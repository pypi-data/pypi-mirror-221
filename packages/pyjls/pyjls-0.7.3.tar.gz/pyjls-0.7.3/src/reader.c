/*
 * Copyright 2021-2022 Jetperch LLC
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include "jls/reader.h"
#include "jls/raw.h"
#include "jls/format.h"
#include "jls/datatype.h"
#include "jls/ec.h"
#include "jls/log.h"
#include "jls/crc32c.h"
#include "jls/rd_fsr.h"
#include "jls/statistics.h"
#include "jls/bit_shift.h"
#include "jls/util.h"
#include <inttypes.h>
#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>
#include <float.h>

#define PAYLOAD_BUFFER_SIZE_DEFAULT (1 << 25)   // 32 MB
#define STRING_BUFFER_SIZE_DEFAULT (1 << 23)    // 8 MB
#define ANNOTATIONS_SIZE_DEFAULT (1 << 20)      // 1 MB
#define F64_BUF_LENGTH_MIN (1 << 16)
#define SIGNAL_MASK  (0x0fff)
#define DECIMATE_PER_DURATION (25)


#define ROE(x)  do {                        \
    int32_t rc__ = (x);                     \
    if (rc__) {                             \
        return rc__;                        \
    }                                       \
} while (0)

#define RLE(x)  do {                        \
    int32_t rc__ = (x);                     \
    if (rc__) {                             \
        JLS_LOGE("error %d: " #x, rc__);    \
        return rc__;                        \
    }                                       \
} while (0)

#if 0
struct source_s {
    struct jls_source_def_s def;
};

struct signal_s {
    struct jls_signal_def_s def;
};

struct jls_rd_s {
    struct source_s * sources[JLS_SOURCE_COUNT];
    struct signal_s * signals[JLS_SIGNAL_COUNT];
    struct jls_chunk_header_s hdr;  // the header for the current chunk
    uint8_t * chunk_buffer;         // storage for the
    size_t chunk_buffer_sz;
    FILE * f;
};
#endif


struct chunk_s {
    struct jls_chunk_header_s hdr;
    int64_t offset;
};

struct payload_s {
    uint8_t * start;
    uint8_t * cur;
    uint8_t * end;  // current end
    size_t length;  // current length
    size_t alloc_size;
};

struct strings_s {
    struct strings_s * next;
    char * start;
    char * cur;
    char * end;
};

struct f64_buf_s {
    double * start;
    double * end;
    size_t alloc_length;  // in double
    double buffer[];
};

struct signal_s {
    int64_t timestamp_start;
    int64_t timestamp_end;
    int64_t track_defs[JLS_TRACK_TYPE_COUNT];
    int64_t track_head_offsets[JLS_TRACK_TYPE_COUNT];
    int64_t track_head_data[JLS_TRACK_TYPE_COUNT][JLS_SUMMARY_LEVEL_COUNT];
    struct jls_rd_fsr_s * rd_fsr;
};

struct jls_rd_s {
    struct jls_raw_s * raw;
    struct jls_source_def_s source_def[JLS_SOURCE_COUNT];
    struct jls_source_def_s source_def_api[JLS_SOURCE_COUNT];
    struct jls_signal_def_s signal_def[JLS_SIGNAL_COUNT];
    struct jls_signal_def_s signal_def_api[JLS_SOURCE_COUNT];
    int64_t signal_length[JLS_SOURCE_COUNT];

    struct signal_s signals[JLS_SIGNAL_COUNT];

    struct chunk_s chunk_cur;
    struct payload_s payload;
    struct strings_s * strings_tail;
    struct strings_s * strings_head;
    struct f64_buf_s * f64_sample_buf;
    struct f64_buf_s * f64_stats_buf;

    struct chunk_s source_head;  // source_def
    struct chunk_s signal_head;  // signal_det, track_*_def, track_*_head

    struct chunk_s user_data_head;  // user_data, ignore first
};

static int32_t strings_alloc(struct jls_rd_s * self) {
    struct strings_s * s = malloc(STRING_BUFFER_SIZE_DEFAULT);
    if (!s) {
        return JLS_ERROR_NOT_ENOUGH_MEMORY;
    }
    char * c8 = (char *) s;
    s->next = NULL;
    s->start = c8 + sizeof(struct strings_s);
    s->cur = s->start;
    s->end = c8 + STRING_BUFFER_SIZE_DEFAULT;
    if (!self->strings_head) {
        self->strings_head = s;
        self->strings_tail = s;
    } else {
        self->strings_tail->next = s;
    }
    return 0;
}

static void strings_free(struct jls_rd_s * self) {
    struct strings_s * s = self->strings_head;
    while (s) {
        struct strings_s * n = s->next;
        free(s);
        s = n;
    }
}

static int32_t f64_buf_alloc(size_t length, struct f64_buf_s ** buf) {
    if (*buf) {
        if ((*buf)->alloc_length >= (size_t) length) {
            return 0;
        } else {
            free(*buf);
            *buf = NULL;
        }
    }

    if (length < F64_BUF_LENGTH_MIN) {
        length = F64_BUF_LENGTH_MIN;
    }
    struct f64_buf_s * b = malloc(sizeof(struct f64_buf_s) + length * sizeof(double));
    if (!b) {
        return JLS_ERROR_NOT_ENOUGH_MEMORY;
    }
    b->start = b->buffer;
    b->end = b->buffer + length;
    b->alloc_length = length;
    *buf = b;
    return 0;
}

static int32_t payload_skip(struct jls_rd_s * self, size_t count) {
    if ((self->payload.cur + count) > self->payload.end) {
        return JLS_ERROR_EMPTY;
    }
    self->payload.cur += count;
    return 0;
}

static int32_t payload_parse_u8(struct jls_rd_s * self, uint8_t * value) {
    if ((self->payload.cur + 1) > self->payload.end) {
        return JLS_ERROR_EMPTY;
    }
    *value = self->payload.cur[0];
    self->payload.cur += 1;
    return 0;
}

static int32_t payload_parse_u16(struct jls_rd_s * self, uint16_t * value) {
    if ((self->payload.cur + 2) > self->payload.end) {
        return JLS_ERROR_EMPTY;
    }
    *value = ((uint16_t) self->payload.cur[0])
            | (((uint16_t) self->payload.cur[1]) << 8);
    self->payload.cur += 2;
    return 0;
}

static int32_t payload_parse_u32(struct jls_rd_s * self, uint32_t * value) {
    if ((self->payload.cur + 4) > self->payload.end) {
        return JLS_ERROR_EMPTY;
    }
    *value = ((uint32_t) self->payload.cur[0])
             | (((uint32_t) self->payload.cur[1]) << 8)
             | (((uint32_t) self->payload.cur[2]) << 16)
             | (((uint32_t) self->payload.cur[3]) << 24);
    self->payload.cur += 4;
    return 0;
}

#if 0

static int32_t payload_parse_u64(struct jls_rd_s * self, uint64_t * value) {
    if ((self->payload.cur + 8) > self->payload.end) {
        return JLS_ERROR_EMPTY;
    }
    *value = ((uint64_t) self->payload.cur[0])
             | (((uint64_t) self->payload.cur[1]) << 8)
             | (((uint64_t) self->payload.cur[2]) << 16)
             | (((uint64_t) self->payload.cur[3]) << 24)
             | (((uint64_t) self->payload.cur[4]) << 32)
             | (((uint64_t) self->payload.cur[5]) << 40)
             | (((uint64_t) self->payload.cur[6]) << 48)
             | (((uint64_t) self->payload.cur[7]) << 56);
    self->payload.cur += 8;
    return 0;
}

#endif

static int32_t payload_parse_str(struct jls_rd_s * self, char ** value) {
    struct strings_s * s = self->strings_tail;
    char * str = s->cur;
    char ch;
    while (self->payload.cur != self->payload.end) {
        if (s->cur >= s->end) {
            ROE(strings_alloc(self));
            // copy over partial.
            while (str <= s->end) {
                *self->strings_tail->cur++ = *str++;
            }
            s = self->strings_tail;
            str = s->start;
        }

        ch = (char) *self->payload.cur++;
        *s->cur++ = ch;
        if (ch == 0) {
            if (*self->payload.cur == 0x1f) {
                self->payload.cur++;
            }
            *value = str;
            return 0;
        }
    }

    *value = NULL;
    return JLS_ERROR_EMPTY;
}

static int32_t rd(struct jls_rd_s * self) {
    while (1) {
        self->chunk_cur.offset = jls_raw_chunk_tell(self->raw);
        int32_t rc = jls_raw_rd(self->raw, &self->chunk_cur.hdr, (uint32_t) self->payload.alloc_size, self->payload.start);
        if (rc == JLS_ERROR_TOO_BIG) {
            size_t sz_new = self->payload.alloc_size;
            while (sz_new < self->chunk_cur.hdr.payload_length) {
                sz_new *= 2;
            }
            uint8_t *ptr = realloc(self->payload.start, sz_new);
            if (!ptr) {
                return JLS_ERROR_NOT_ENOUGH_MEMORY;
            }
            self->payload.start = ptr;
            self->payload.cur = ptr;
            self->payload.end = ptr;
            self->payload.length = 0;
            self->payload.alloc_size = sz_new;
        } else if (rc == 0) {
            self->payload.cur = self->payload.start;
            self->payload.length = self->chunk_cur.hdr.payload_length;
            self->payload.end = self->payload.start + self->payload.length;
            return 0;
        } else {
            return rc;
        }
    }
}

static int32_t scan_sources(struct jls_rd_s * self) {
    JLS_LOGD1("scan_sources");
    ROE(jls_raw_chunk_seek(self->raw, self->source_head.offset));
    while (1) {
        ROE(rd(self));
        uint16_t source_id = self->chunk_cur.hdr.chunk_meta;
        if (source_id >= JLS_SOURCE_COUNT) {
            JLS_LOGW("source_id %d too big - skip", (int) source_id);
        } else {
            struct jls_source_def_s *src = &self->source_def[source_id];
            ROE(payload_skip(self, 64));
            ROE(payload_parse_str(self, (char **) &src->name));
            ROE(payload_parse_str(self, (char **) &src->vendor));
            ROE(payload_parse_str(self, (char **) &src->model));
            ROE(payload_parse_str(self, (char **) &src->version));
            ROE(payload_parse_str(self, (char **) &src->serial_number));
            src->source_id = source_id;  // indicate that this source is valid!
            JLS_LOGD1("Found source %d : %s", (int) source_id, src->name);
        }
        if (!self->chunk_cur.hdr.item_next) {
            break;
        }
        ROE(jls_raw_chunk_seek(self->raw, self->chunk_cur.hdr.item_next));
    }
    return 0;
}

static int32_t signal_validate(struct jls_rd_s * self, uint16_t signal_id, struct jls_signal_def_s * s) {
    if (signal_id >= JLS_SIGNAL_COUNT) {
        JLS_LOGW("signal_id %d too big - skip", (int) signal_id);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    if (self->source_def[s->source_id].source_id != s->source_id) {
        JLS_LOGW("signal %d: source_id %d not found", (int) signal_id, (int) s->source_id);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    switch (s->signal_type) {
        case JLS_SIGNAL_TYPE_FSR: break;
        case JLS_SIGNAL_TYPE_VSR: break;
        default:
            JLS_LOGW("signal %d: invalid signal_type: %d", (int) signal_id, (int) s->signal_type);
            return JLS_ERROR_PARAMETER_INVALID;
    }

    // todo check data_type
    return 0;
}

static int32_t handle_signal_def(struct jls_rd_s * self) {
    uint16_t signal_id = self->chunk_cur.hdr.chunk_meta;
    if (signal_id >= JLS_SIGNAL_COUNT) {
        JLS_LOGW("signal_id %d too big - skip", (int) signal_id);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    struct jls_signal_def_s *s = &self->signal_def[signal_id];
    s->signal_id = signal_id;
    ROE(payload_parse_u16(self, &s->source_id));
    ROE(payload_parse_u8(self, &s->signal_type));
    ROE(payload_skip(self, 1));
    ROE(payload_parse_u32(self, &s->data_type));
    ROE(payload_parse_u32(self, &s->sample_rate));
    ROE(payload_parse_u32(self, &s->samples_per_data));
    ROE(payload_parse_u32(self, &s->sample_decimate_factor));
    ROE(payload_parse_u32(self, &s->entries_per_summary));
    ROE(payload_parse_u32(self, &s->summary_decimate_factor));
    ROE(payload_parse_u32(self, &s->annotation_decimate_factor));
    ROE(payload_parse_u32(self, &s->utc_decimate_factor));
    ROE(payload_skip(self, 92));
    ROE(payload_parse_str(self, (char **) &s->name));
    ROE(payload_parse_str(self, (char **) &s->units));
    if (0 == signal_validate(self, signal_id, s)) {  // validate passed
        s->signal_id = signal_id;  // indicate that this signal is valid
        JLS_LOGD1("Found signal %d : %s", (int) signal_id, s->name);
    }  // else skip
    return 0;
}

static bool is_signal_defined(struct jls_rd_s * self, uint16_t signal_id) {
    signal_id &= SIGNAL_MASK;  // mask off chunk_meta depth
    if (signal_id >= JLS_SIGNAL_COUNT) {
        JLS_LOGW("signal_id %d too big", (int) signal_id);
        return false;
    }
    if (self->signal_def[signal_id].signal_id != signal_id) {
        JLS_LOGW("signal_id %d not defined", (int) signal_id);
        return false;
    }
    return true;
}

static bool is_signal_defined_type(struct jls_rd_s * self, uint16_t signal_id, enum jls_signal_type_e type) {
    if (!is_signal_defined(self, signal_id)) {
        return false;
    }
    return self->signal_def[signal_id].signal_type == type;
}

static inline uint8_t tag_parse_track_type(uint8_t tag) {
    return (tag >> 3) & 3;
}

static int32_t validate_track_tag(struct jls_rd_s * self, uint16_t signal_id, uint8_t tag) {
    if (!is_signal_defined(self, signal_id)) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    struct jls_signal_def_s * signal_def = &self->signal_def[signal_id];
    uint8_t track_type = tag_parse_track_type(tag);
    switch (signal_def->signal_type) {
        case JLS_SIGNAL_TYPE_FSR:
            if ((track_type == JLS_TRACK_TYPE_FSR)
                || (track_type == JLS_TRACK_TYPE_ANNOTATION)
                || (track_type == JLS_TRACK_TYPE_UTC)) {
                // good
            } else {
                JLS_LOGW("unsupported track %d for FSR signal", (int) track_type);
                return JLS_ERROR_PARAMETER_INVALID;
            }
            break;
        case JLS_SIGNAL_TYPE_VSR:
            if ((track_type == JLS_TRACK_TYPE_VSR)
                || (track_type == JLS_TRACK_TYPE_ANNOTATION)) {
                // good
            } else {
                JLS_LOGW("unsupported track %d for VSR signal", (int) track_type);
                return JLS_ERROR_PARAMETER_INVALID;
            }
            break;
        default:
            // should have already been checked.
            JLS_LOGW("unsupported signal type: %d", (int) signal_def->signal_type);
            return JLS_ERROR_PARAMETER_INVALID;
    }
    return 0;
}

static int32_t handle_track_def(struct jls_rd_s * self, int64_t pos) {
    uint16_t signal_id = self->chunk_cur.hdr.chunk_meta & SIGNAL_MASK;
    ROE(validate_track_tag(self, signal_id, self->chunk_cur.hdr.tag));
    self->signals[signal_id].track_defs[tag_parse_track_type(self->chunk_cur.hdr.tag)] = pos;
    return 0;
}

static int32_t handle_track_head(struct jls_rd_s * self, int64_t pos) {
    uint16_t signal_id = self->chunk_cur.hdr.chunk_meta & SIGNAL_MASK;
    ROE(validate_track_tag(self, signal_id, self->chunk_cur.hdr.tag));
    uint8_t track_type = tag_parse_track_type(self->chunk_cur.hdr.tag);

    self->signals[signal_id].track_head_offsets[track_type] = pos;
    size_t expect_sz = JLS_SUMMARY_LEVEL_COUNT * sizeof(int64_t);

    if (self->payload.length != expect_sz) {
        JLS_LOGW("cannot parse signal %d head, sz=%zu, expect=%zu",
                 (int) signal_id, self->payload.length, expect_sz);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    memcpy(self->signals[signal_id].track_head_data[track_type], self->payload.start, expect_sz);
    return 0;
}

static int32_t scan_signals(struct jls_rd_s * self) {
    JLS_LOGD1("scan_signals");
    ROE(jls_raw_chunk_seek(self->raw, self->signal_head.offset));
    while (1) {
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag == JLS_TAG_SIGNAL_DEF) {
            handle_signal_def(self);
        } else if ((self->chunk_cur.hdr.tag & 7) == JLS_TRACK_CHUNK_DEF) {
            handle_track_def(self, self->chunk_cur.offset);
        } else if ((self->chunk_cur.hdr.tag & 7) == JLS_TRACK_CHUNK_HEAD) {
            handle_track_head(self, self->chunk_cur.offset);
        } else {
            JLS_LOGW("unknown tag %d in signal list", (int) self->chunk_cur.hdr.tag);
        }
        if (!self->chunk_cur.hdr.item_next) {
            break;
        }
        ROE(jls_raw_chunk_seek(self->raw, self->chunk_cur.hdr.item_next));
    }
    return 0;
}

static int32_t scan_fsr_sample_id(struct jls_rd_s * self) {
    JLS_LOGD1("scan_fsr_sample_id");
    for (uint32_t signal_id = 1; signal_id < JLS_SIGNAL_COUNT; ++signal_id) {
        if ((self->signal_def[signal_id].signal_id != signal_id)
                || (self->signal_def[signal_id].signal_type != JLS_SIGNAL_TYPE_FSR)) {
            continue;
        }
        struct signal_s * s = &self->signals[signal_id];
        int64_t offset = s->track_head_data[JLS_TRACK_TYPE_FSR][0];
        if (offset == 0) {
            continue;  // no data
        }
        ROE(jls_raw_chunk_seek(self->raw, offset));
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag != JLS_TAG_TRACK_FSR_DATA) {
            JLS_LOGW("scan_fsr_sample_id tag mismatch: %d", (int) self->chunk_cur.hdr.tag);
            continue;
        }

        struct jls_fsr_data_s * r = (struct jls_fsr_data_s *) self->payload.start;
        self->signal_def[signal_id].sample_id_offset = r->header.timestamp;
    }
    return 0;
}

static int32_t scan(struct jls_rd_s * self) {
    int32_t rc = 0;
    uint8_t found = 0;

    for (int i = 0; found != 7; ++i) {
        if (i == 3) {
            JLS_LOGW("malformed JLS, continue searching");
        }
        int64_t pos = jls_raw_chunk_tell(self->raw);
        rc = rd(self);
        if (rc == JLS_ERROR_EMPTY) {
            return 0;
        } else if (rc) {
            return rc;
        }

        JLS_LOGD1("scan tag %d : %s", self->chunk_cur.hdr.tag, jls_tag_to_name(self->chunk_cur.hdr.tag));
        switch (self->chunk_cur.hdr.tag) {
            case JLS_TAG_USER_DATA:
                found |= 1;
                if (!self->user_data_head.offset) {
                    self->user_data_head.offset = pos;
                    self->user_data_head.hdr = self->chunk_cur.hdr;
                }
                break;
            case JLS_TAG_SOURCE_DEF:
                found |= 2;
                if (!self->source_head.offset) {
                    self->source_head.offset = pos;
                    self->source_head.hdr = self->chunk_cur.hdr;
                }
                break;
            case JLS_TAG_SIGNAL_DEF:
                found |= 4;
                if (!self->signal_head.offset) {
                    self->signal_head.offset = pos;
                    self->signal_head.hdr = self->chunk_cur.hdr;
                }
                break;
            default:
                break;  // skip
        }
    }
    JLS_LOGD1("found initial tags");
    ROE(scan_sources(self));
    ROE(scan_signals(self));
    ROE(scan_fsr_sample_id(self));
    return 0;
}

int32_t jls_rd_open(struct jls_rd_s ** instance, const char * path) {
    if (!instance) {
        return JLS_ERROR_PARAMETER_INVALID;
    }

    struct jls_rd_s *self = calloc(1, sizeof(struct jls_rd_s));
    if (!self) {
        return JLS_ERROR_NOT_ENOUGH_MEMORY;
    }

    for (int32_t k = 0; k < JLS_SOURCE_COUNT; ++k) {
        self->signal_length[k] = -1;
    }

    self->payload.start = malloc(PAYLOAD_BUFFER_SIZE_DEFAULT);
    strings_alloc(self);

    if (!self->payload.start || !self->strings_head) {
        jls_rd_close(self);
        return JLS_ERROR_NOT_ENOUGH_MEMORY;
    }
    self->payload.alloc_size = PAYLOAD_BUFFER_SIZE_DEFAULT;
    self->payload.cur = self->payload.start;
    self->payload.end = self->payload.start;

    int32_t rc = jls_raw_open(&self->raw, path, "r");
    if (rc) {
        jls_rd_close(self);
        return rc;
    }

    if (jls_raw_version(self->raw).s.major < 1) {
        JLS_LOGE("version < 1.x.x no longer supported");
        return JLS_ERROR_UNSUPPORTED_FILE;
    }

    int64_t end_pos = jls_raw_chunk_tell_end(self->raw);
    if (!end_pos) {
        JLS_LOGW("not properly closed");
        // Not properly closed.  Indices & summary may be incomplete.
        // for most applications, will want to launch file reconstruction tool
        return JLS_ERROR_MESSAGE_INTEGRITY;
    }

    ROE(scan(self));
    *instance = self;
    return rc;
}

void jls_rd_close(struct jls_rd_s * self) {
    if (self) {
        jls_raw_close(self->raw);
        strings_free(self);
        if (self->payload.start) {
            free(self->payload.start);
            self->payload.start = NULL;
        }
        if (self->f64_stats_buf) {
            free(self->f64_stats_buf);
            self->f64_stats_buf = NULL;
        }
        if (self->f64_sample_buf) {
            free(self->f64_sample_buf);
            self->f64_sample_buf = NULL;
        }
        self->raw = NULL;
        free(self);
    }
}

int32_t jls_rd_sources(struct jls_rd_s * self, struct jls_source_def_s ** sources, uint16_t * count) {
    if (!self || !sources || !count) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    uint16_t c = 0;
    for (uint16_t i = 0; i < JLS_SOURCE_COUNT; ++i) {
        if (self->source_def[i].source_id == i) {
            // Note: source 0 is always defined, so calloc is ok
            self->source_def_api[c++] = self->source_def[i];
        }
    }
    *sources = self->source_def_api;
    *count = c;
    return 0;
}

int32_t jls_rd_signals(struct jls_rd_s * self, struct jls_signal_def_s ** signals, uint16_t * count) {
    if (!self || !signals || !count) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    uint16_t c = 0;
    for (uint16_t i = 0; i < JLS_SIGNAL_COUNT; ++i) {
        if (self->signal_def[i].signal_id == i) {
            // Note: signal 0 is always defined, so calloc is ok
            self->signal_def_api[c++] = self->signal_def[i];
        }
    }
    *signals = self->signal_def_api;
    *count = c;
    return 0;
}

int32_t jls_rd_signal(struct jls_rd_s * self, uint16_t signal_id, struct jls_signal_def_s * signal) {
    if (!is_signal_defined(self, signal_id)) {
        return JLS_ERROR_NOT_FOUND;
    }
    if (signal) {
        *signal = self->signal_def[signal_id];
    }
    return 0;
}

static int32_t ts_seek(struct jls_rd_s * self, uint16_t signal_id, uint8_t level,
                       enum jls_track_type_e track_type, int64_t timestamp) {
    // timestamp in JLS units with possible non-zero offset
    if (!is_signal_defined(self, signal_id)) {
        return JLS_ERROR_NOT_FOUND;
    }
    switch (track_type) {
        case JLS_TRACK_TYPE_VSR: break;
        case JLS_TRACK_TYPE_ANNOTATION: break;
        case JLS_TRACK_TYPE_UTC: break;
        default:
            JLS_LOGW("ts_seek: unsupported track type: %d", (int) track_type);
            return JLS_ERROR_PARAMETER_INVALID;
    }
    struct signal_s * s = &self->signals[signal_id];
    int64_t offset = 0;
    int64_t * offsets = s->track_head_data[track_type];

    int initial_level = JLS_SUMMARY_LEVEL_COUNT - 1;
    for (; initial_level >= 0; --initial_level) {
        if (offsets[initial_level]) {
            offset = offsets[initial_level];
            break;
        }
    }
    if (!offset) {
        return JLS_ERROR_NOT_FOUND;
    }

    for (int lvl = initial_level; lvl > level; --lvl) {
        JLS_LOGD3("signal %d, level %d, offset=%" PRIi64, (int) signal_id, (int) lvl, offset);
        ROE(jls_raw_chunk_seek(self->raw, offset));
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag != jls_track_tag_pack(track_type, JLS_TRACK_CHUNK_INDEX)) {
            JLS_LOGW("seek tag mismatch: %d", (int) self->chunk_cur.hdr.tag);
        }

        struct jls_index_s * r = (struct jls_index_s *) self->payload.start;
        uint8_t * p_end = (uint8_t *) &r->entries[r->header.entry_count];

        if ((size_t) (p_end - self->payload.start) > self->payload.length) {
            JLS_LOGE("invalid payload length");
            return JLS_ERROR_PARAMETER_INVALID;
        }
        if ((r->header.entry_count == 0) || (r->header.entry_count & 0x80000000)) {
            JLS_LOGE("invalid entry count");
            return JLS_ERROR_PARAMETER_INVALID;
        }

        int32_t idx = 0;
        for (; ; ++idx) {
            if (idx >= (int32_t) r->header.entry_count) {
                idx = ((int32_t) r->header.entry_count) - 1;
                break;
            } else if (r->entries[idx].timestamp> timestamp) {
                --idx;
                break;
            } else if (r->entries[idx].timestamp == timestamp) {
                break;
            }
        }
        if (idx < 0) {
            idx = 0;
        }
        offset = r->entries[idx].offset;
    }

    ROE(jls_raw_chunk_seek(self->raw, offset));
    return 0;
}

static int32_t fsr_seek(struct jls_rd_s * self, uint16_t signal_id, uint8_t level, int64_t sample_id) {
    // timestamp in JLS units with possible non-zero offset
    if (!is_signal_defined(self, signal_id)) {
        return JLS_ERROR_NOT_FOUND;
    }
    struct jls_signal_def_s * signal_def = &self->signal_def[signal_id];
    if (signal_def->signal_type != JLS_SIGNAL_TYPE_FSR) {
        JLS_LOGW("fsr_seek not support for signal type %d", (int) signal_def->signal_type);
        return JLS_ERROR_NOT_SUPPORTED;
    }
    struct signal_s * s = &self->signals[signal_id];
    int64_t offset = 0;
    int64_t * offsets = s->track_head_data[JLS_TRACK_TYPE_FSR];
    int initial_level = JLS_SUMMARY_LEVEL_COUNT - 1;
    for (; initial_level >= 0; --initial_level) {
        if (offsets[initial_level]) {
            offset = offsets[initial_level];
            break;
        }
    }
    if (!offset) {
        return JLS_ERROR_NOT_FOUND;
    }

    for (int lvl = initial_level; lvl > level; --lvl) {
        // compute the step size in samples between each index entry.
        int64_t step_size = signal_def->samples_per_data;  // each data chunk
        if (lvl > 1) {
            step_size *= signal_def->entries_per_summary /
                    (signal_def->samples_per_data / signal_def->sample_decimate_factor);
        }
        for (int k = 3; k <= lvl; ++k) {
            step_size *= signal_def->summary_decimate_factor;
        }
        JLS_LOGD3("signal %d, level %d, offset=%" PRIi64 ", step_size=%" PRIi64,
                 (int) signal_id, lvl, offset, step_size);
        ROE(jls_raw_chunk_seek(self->raw, offset));
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag != JLS_TAG_TRACK_FSR_INDEX) {
            JLS_LOGW("seek tag mismatch: %d", (int) self->chunk_cur.hdr.tag);
        }

        struct jls_fsr_index_s * r = (struct jls_fsr_index_s *) self->payload.start;
        int64_t chunk_timestamp = r->header.timestamp;
        int64_t chunk_entries = r->header.entry_count;
        JLS_LOGD3("timestamp=%" PRIi64 ", entries=%" PRIi64, chunk_timestamp, chunk_entries);
        uint8_t * p_end = (uint8_t *) &r->offsets[r->header.entry_count];

        if ((size_t) (p_end - self->payload.start) > self->payload.length) {
            JLS_LOGE("invalid payload length");
            return JLS_ERROR_PARAMETER_INVALID;
        }

        int64_t idx = (sample_id - chunk_timestamp) / step_size;
        if ((idx < 0) || (idx >= chunk_entries)) {
            JLS_LOGE("invalid index signal %d, level %d, sample_id=%"
                     PRIi64 " offset=%" PRIi64 ": %" PRIi64 " >= %" PRIi64,
                     (int) signal_id, lvl, sample_id,
                     offset, idx, chunk_entries);
            return JLS_ERROR_IO;
        }
        offset = r->offsets[idx];
    }

    ROE(jls_raw_chunk_seek(self->raw, offset));
    return 0;
}


int32_t jls_rd_fsr_length(struct jls_rd_s * self, uint16_t signal_id, int64_t * samples) {
    if (!is_signal_defined_type(self, signal_id, JLS_SIGNAL_TYPE_FSR)) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    if (self->signal_length[signal_id] >= 0) {
        *samples = self->signal_length[signal_id];
        return 0;
    }

    struct signal_s * s = &self->signals[signal_id];
    int64_t offset = 0;
    int64_t * offsets = s->track_head_data[JLS_TRACK_TYPE_FSR];
    int level = JLS_SUMMARY_LEVEL_COUNT - 1;
    for (; level >= 0; --level) {
        if (offsets[level]) {
            offset = offsets[level];
            break;
        }
    }
    if (!offset) {
        *samples = 0;
        return 0;
    }
    struct jls_fsr_index_s * r;

    for (int lvl = level; lvl > 0; --lvl) {
        JLS_LOGD3("signal %d, level %d, index=%" PRIi64, (int) signal_id, (int) lvl, offset);
        ROE(jls_raw_chunk_seek(self->raw, offset));
        ROE(rd(self));

        r = (struct jls_fsr_index_s *) self->payload.start;
        if (r->header.entry_size_bits != (sizeof(r->offsets[0]) * 8)) {
            JLS_LOGE("invalid FSR index entry size: %d bits", (int) r->header.entry_size_bits);
            return JLS_ERROR_PARAMETER_INVALID;
        }
        size_t sz = sizeof(r->header) + r->header.entry_count * sizeof(r->offsets[0]);
        if (sz > self->payload.length) {
            JLS_LOGE("invalid payload length");
            return JLS_ERROR_PARAMETER_INVALID;
        }
        if (r->header.entry_count > 0) {
            offset = r->offsets[r->header.entry_count - 1];
        }
    }

    ROE(jls_raw_chunk_seek(self->raw, offset));
    ROE(rd(self));
    r = (struct jls_fsr_index_s *) self->payload.start;
    self->signal_length[signal_id] = r->header.timestamp + r->header.entry_count
            - self->signal_def[signal_id].sample_id_offset;
    *samples = self->signal_length[signal_id];
    return 0;
}

int32_t jls_rd_fsr(struct jls_rd_s * self, uint16_t signal_id, int64_t start_sample_id,
                   void * data, int64_t data_length) {
    // start_sample_id is API zero-based
    const int64_t data_length_orig = data_length;
    int32_t rv = 0;
    uint8_t * data_u8 = (uint8_t *) data;
    if (!is_signal_defined_type(self, signal_id, JLS_SIGNAL_TYPE_FSR)) {
        JLS_LOGW("signal_id %d invalid", (int) signal_id);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    int64_t samples = 0;
    ROE(jls_rd_fsr_length(self, signal_id, &samples));
    struct jls_signal_def_s * signal_def = &self->signal_def[signal_id];
    if (data_length <= 0) {
        return 0;
    } else if (start_sample_id < 0) {
        JLS_LOGW("rd_fsr %d %s: start_sample_id invalid %" PRIi64 " length=%" PRIi64,
                 (int) signal_id, signal_def->name,
                 start_sample_id, samples);
        return JLS_ERROR_PARAMETER_INVALID;
    }

    const int64_t sample_id_offset = self->signal_def[signal_id].sample_id_offset;
    uint8_t entry_size_bits = jls_datatype_parse_size(signal_def->data_type);

    if ((start_sample_id + data_length) > samples) {
        JLS_LOGW("rd_fsr %d %s: start=%" PRIi64 " length=%" PRIi64 " > %" PRIi64 " by %" PRIi64,
                 (int) signal_id, signal_def->name,
                 start_sample_id, data_length, samples,
                 start_sample_id + data_length - samples);
        return JLS_ERROR_PARAMETER_INVALID;
    }

    uint8_t shift_right_bits = 0;
    if (entry_size_bits < 8) {
        int64_t sample_id = start_sample_id;
        switch (entry_size_bits) {
            case 1:
                sample_id &= ~0x07;
                if (sample_id != start_sample_id) {
                    shift_right_bits = (uint8_t) (start_sample_id - sample_id);
                }
                break;
            case 4:
                sample_id &= ~0x01;
                if (sample_id != start_sample_id) {
                    shift_right_bits = 4;
                }
                break;
            default:
                JLS_LOGW("entry_size_bits invalid: %d", (int) entry_size_bits);
                return JLS_ERROR_PARAMETER_INVALID;
        }
        data_length += start_sample_id - sample_id;
        start_sample_id = sample_id;
    }

    //JLS_LOGD3("jls_rd_fsr_f32(%d, %" PRIi64 ")", (int) signal_id, start_sample_id);
    start_sample_id += sample_id_offset;  // file sample_id
    ROE(fsr_seek(self, signal_id, 0, start_sample_id));
    self->chunk_cur.hdr.item_next = jls_raw_chunk_tell(self->raw);
    while (data_length > 0) {
        if (jls_raw_chunk_seek(self->raw, self->chunk_cur.hdr.item_next)) {
            return JLS_ERROR_NOT_FOUND;
        }
        rv = rd(self);
        if (rv == JLS_ERROR_EMPTY) {
            return JLS_ERROR_NOT_FOUND;
        } else if (rv) {
            return rv;
        }
        struct jls_fsr_data_s * r = (struct jls_fsr_data_s *) self->payload.start;
        int64_t chunk_sample_id = r->header.timestamp;
        int64_t chunk_sample_count = r->header.entry_count;
        if (r->header.entry_size_bits != entry_size_bits) {
            JLS_LOGE("fsr entry size mismatch");
            return JLS_ERROR_UNSPECIFIED;
        }
        int64_t idx_start = 0;
        if (start_sample_id > chunk_sample_id) {
            idx_start = start_sample_id - chunk_sample_id;
        }
        chunk_sample_count -= idx_start;
        if (data_length < chunk_sample_count) {
            chunk_sample_count = data_length;
        }
        uint8_t * u8 = (uint8_t *) &r->data[0];
        size_t sz_bytes = (size_t) (chunk_sample_count * entry_size_bits + 7) / 8;
        size_t u8_offset = (size_t) ((idx_start * entry_size_bits) / 8);
        memcpy(data_u8, u8 + u8_offset, sz_bytes);
        data_u8 += sz_bytes;
        data_length -= chunk_sample_count;
    }

    if (shift_right_bits) {
        jls_bit_shift_array_right(shift_right_bits, data, (size_t) ((data_length_orig * entry_size_bits + shift_right_bits + 7) / 8));
    }

    return 0;
}

JLS_API int32_t jls_rd_fsr_f32(struct jls_rd_s * self, uint16_t signal_id, int64_t start_sample_id,
                               float * data, int64_t data_length) {
    if (!is_signal_defined_type(self, signal_id, JLS_SIGNAL_TYPE_FSR)) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    if (self->signal_def[signal_id].data_type != JLS_DATATYPE_F32) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    return jls_rd_fsr(self, signal_id, start_sample_id, data, data_length);
}

static inline void f32_to_stats(struct jls_statistics_s * stats, const float * data, int64_t count) {
    stats->k = count;
    stats->mean = data[JLS_SUMMARY_FSR_MEAN];
    stats->min = data[JLS_SUMMARY_FSR_MIN];
    stats->max = data[JLS_SUMMARY_FSR_MAX];
    if (count > 1) {
        stats->s = ((double) data[JLS_SUMMARY_FSR_STD]) * data[JLS_SUMMARY_FSR_STD] * (count - 1);
    } else {
        stats->s = 0.0;
    }
}

static inline void stats_to_f64(double * data, struct jls_statistics_s * stats) {
    data[JLS_SUMMARY_FSR_MEAN] = stats->mean;
    data[JLS_SUMMARY_FSR_MIN] = stats->min;
    data[JLS_SUMMARY_FSR_MAX] = stats->max;
    data[JLS_SUMMARY_FSR_STD] = sqrt(jls_statistics_var(stats));
}

static inline void f64_to_stats(struct jls_statistics_s * stats, const double * data, int64_t count) {
    stats->k = count;
    stats->mean = data[JLS_SUMMARY_FSR_MEAN];
    stats->min = data[JLS_SUMMARY_FSR_MIN];
    stats->max = data[JLS_SUMMARY_FSR_MAX];
    if (count > 1) {
        stats->s = ((double) data[JLS_SUMMARY_FSR_STD]) * data[JLS_SUMMARY_FSR_STD] * (count - 1);
    } else {
        stats->s = 0.0;
    }
}

static int32_t rd_stats_chunk(struct jls_rd_s * self, uint16_t signal_id, uint8_t level) {
    ROE(rd(self));
    if (JLS_TAG_TRACK_FSR_SUMMARY != self->chunk_cur.hdr.tag) {
        JLS_LOGW("unexpected chunk tag %d", (int) self->chunk_cur.hdr.tag);
        return JLS_ERROR_IO;
    }
    uint16_t metadata = (signal_id & SIGNAL_MASK) | (((uint16_t) level) << 12);
    if (metadata != self->chunk_cur.hdr.chunk_meta) {
        JLS_LOGW("unexpected chunk meta 0x%04x", (unsigned int) self->chunk_cur.hdr.chunk_meta);
        return JLS_ERROR_IO;
    }

    /*
    // display stats chunk data
    int64_t *i64 = (int64_t *) self->payload.start;
    JLS_LOGI("stats chunk: sample_id=%" PRIi64 ", entries=%" PRIi64, i64[0], i64[1]);
    float * d = (float *) &i64[2];
    for (int64_t i = 0; i < i64[1] * 4; i += 4) {
        JLS_LOGI("stats: mean=%f min=%f max=%f std=%f",
            d[i + JLS_SUMMARY_FSR_MEAN],
            d[i + JLS_SUMMARY_FSR_MIN],
            d[i + JLS_SUMMARY_FSR_MAX],
            d[i + JLS_SUMMARY_FSR_STD]);
    }
    */
    return 0;
}

static int32_t fsr_statistics(struct jls_rd_s * self, uint16_t signal_id,
                              int64_t start_sample_id, int64_t increment, uint8_t level,
                              double * data, int64_t data_length) {
    // start_sample_id in JLS units with possible non-zero offset
    JLS_LOGD2("fsr_f32_statistics(signal_id=%d, start_id=%" PRIi64 ", incr=%" PRIi64 ", level=%d, len=%" PRIi64 ")",
              (int) signal_id, start_sample_id, increment, (int) level, data_length);
    bool is_f32;
    struct jls_signal_def_s * signal_def = &self->signal_def[signal_id];
    int64_t step_size = signal_def->sample_decimate_factor;
    for (uint8_t lvl = 2; lvl <= level; ++lvl) {
        step_size *= signal_def->summary_decimate_factor;
    }
    double f64_tmp4[JLS_SUMMARY_FSR_COUNT];
    const int64_t sample_id_offset = self->signal_def[signal_id].sample_id_offset;

    ROE(fsr_seek(self, signal_id, level, start_sample_id)); // returns the index
    ROE(jls_raw_chunk_next(self->raw));  // statistics
    int64_t pos = jls_raw_chunk_tell(self->raw);
    ROE(rd_stats_chunk(self, signal_id, level));

    struct jls_fsr_f32_summary_s * f32_summary = (struct jls_fsr_f32_summary_s *) self->payload.start;
    struct jls_fsr_f64_summary_s * f64_summary = (struct jls_fsr_f64_summary_s *) self->payload.start;
    int64_t chunk_sample_id = f32_summary->header.timestamp;
    if (f32_summary->header.entry_size_bits == JLS_SUMMARY_FSR_COUNT * sizeof(float) * 8) {
        is_f32 = true;  // 32-bit float summaries
    } else if (f32_summary->header.entry_size_bits == JLS_SUMMARY_FSR_COUNT * sizeof(double) * 8) {
        is_f32 = false; // 64-bit float summaries
    } else {
        JLS_LOGE("invalid summary entry size: %d", (int) f32_summary->header.entry_size_bits);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    int64_t src_offset = 0;
    int64_t src_end = f32_summary->header.entry_count;
    int64_t entry_offset = ((start_sample_id - chunk_sample_id + step_size - 1) / step_size);
    int64_t entry_sample_id = entry_offset * step_size + chunk_sample_id;

    struct jls_statistics_s stats_accum;
    jls_statistics_reset(&stats_accum);
    struct jls_statistics_s stats_next;

    int64_t incr_remaining = increment;

    if (entry_sample_id != start_sample_id) {
        int64_t incr = entry_sample_id - start_sample_id;
        // invalidates stats, need to reload, providing API sample_id
        ROE(jls_rd_fsr_statistics(self, signal_id, start_sample_id - sample_id_offset,
                                  incr, f64_tmp4, 1));
        ROE(jls_raw_chunk_seek(self->raw, pos));
        ROE(rd_stats_chunk(self, signal_id, level));
        f64_to_stats(&stats_accum, f64_tmp4, incr);
        incr_remaining -= incr;
        start_sample_id += incr;
    }
    src_offset += entry_offset;

    while (data_length) {
        if (src_offset >= src_end) {
            if (self->chunk_cur.hdr.item_next) {
                ROE(jls_raw_chunk_seek(self->raw, self->chunk_cur.hdr.item_next));
                ROE(rd_stats_chunk(self, signal_id, level));
                f32_summary = (struct jls_fsr_f32_summary_s *) self->payload.start;
                f64_summary = (struct jls_fsr_f64_summary_s *) self->payload.start;
                if (f32_summary->header.entry_size_bits == JLS_SUMMARY_FSR_COUNT * sizeof(float) * 8) {
                    is_f32 = true;  // 32-bit float summaries
                } else if (f32_summary->header.entry_size_bits == JLS_SUMMARY_FSR_COUNT * sizeof(double) * 8) {
                    is_f32 = false; // 64-bit float summaries
                } else {
                    JLS_LOGE("invalid summary entry size: %d", (int) f32_summary->header.entry_size_bits);
                    return JLS_ERROR_PARAMETER_INVALID;
                }
                src_offset = 0;
                src_end = f32_summary->header.entry_count;
            } else {
                if ((incr_remaining <= step_size) && (data_length == 1)) {
                    // not a problem, will fetch from lower statistics
                } else {
                    JLS_LOGW("cannot get final %" PRIi64 " samples", data_length);
                    for (int64_t idx = 0; idx < (JLS_SUMMARY_FSR_COUNT * data_length); ++idx) {
                        data[idx] = NAN;
                    }
                    return JLS_ERROR_PARAMETER_INVALID;
                }
            }
        }

        if (incr_remaining <= step_size) {
            if (data_length == 1) {
                ROE(jls_rd_fsr_statistics(self, signal_id, start_sample_id - sample_id_offset,
                                          incr_remaining, f64_tmp4, 1));
                f64_to_stats(&stats_next, f64_tmp4, incr_remaining);
            } else if (is_f32) {
                f32_to_stats(&stats_next, f32_summary->data[src_offset], incr_remaining);
            } else {
                f64_to_stats(&stats_next, f64_summary->data[src_offset], incr_remaining);
            }
            jls_statistics_combine(&stats_accum, &stats_accum, &stats_next);
            stats_to_f64(data, &stats_accum);
            data += JLS_SUMMARY_FSR_COUNT;
            --data_length;
            int64_t incr = step_size - incr_remaining;
            if (incr < 0) {
                JLS_LOGE("internal error");
                incr = 0;
                jls_statistics_reset(&stats_accum);
            } else if (incr == 0) {
                jls_statistics_reset(&stats_accum);
            } else if (is_f32) {
                f32_to_stats(&stats_accum, f32_summary->data[src_offset], incr);
            } else {
                f64_to_stats(&stats_accum, f64_summary->data[src_offset], incr);
            }
            incr_remaining = increment - incr;
        } else {
            if (is_f32) {
                f32_to_stats(&stats_next, f32_summary->data[src_offset], step_size);
            } else {
                f64_to_stats(&stats_next, f64_summary->data[src_offset], step_size);
            }
            jls_statistics_combine(&stats_accum, &stats_accum, &stats_next);
            incr_remaining -= step_size;
        }
        start_sample_id += step_size;
        ++src_offset;
    }
    return 0;
}

int32_t jls_rd_fsr_statistics(struct jls_rd_s * self, uint16_t signal_id,
                              int64_t start_sample_id, int64_t increment,
                              double * data, int64_t data_length) {
    // API zero-based start_sample_id
    if (!is_signal_defined_type(self, signal_id, JLS_SIGNAL_TYPE_FSR)) {
        JLS_LOGW("signal_id %d invalid", (int) signal_id);
        return JLS_ERROR_PARAMETER_INVALID;
    } else if (increment <= 0) {
        JLS_LOGW("invalid increment: %" PRIi64, increment);
        return JLS_ERROR_PARAMETER_INVALID;
    } else if (data_length <= 0) {
        JLS_LOGW("invalid length: %" PRIi64, data_length);
        return 0;
    } else if (start_sample_id < 0) {
        JLS_LOGW("invalid start_sample_id: %" PRIi64, start_sample_id);
        return JLS_ERROR_PARAMETER_INVALID;
    }

    int64_t samples = 0;
    ROE(jls_rd_fsr_length(self, signal_id, &samples));
    int64_t end_sample_id = start_sample_id + increment * data_length;
    if (end_sample_id > samples) {
        JLS_LOGW("invalid length: %" PRIi64 " > %" PRIi64, end_sample_id, samples);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    const int64_t sample_id_offset = self->signal_def[signal_id].sample_id_offset;

    struct jls_signal_def_s * signal_def = &self->signal_def[signal_id];
    uint8_t level = 0;
    int64_t sample_multiple_next = signal_def->sample_decimate_factor;
    int64_t duration = increment * data_length;
    while ((increment >= sample_multiple_next)
            && (duration >= (DECIMATE_PER_DURATION * sample_multiple_next))) {
        ++level;
        sample_multiple_next *= signal_def->summary_decimate_factor;
    }
    start_sample_id += sample_id_offset; // JLS file sample_id

    if (level) {  // use summaries
        return fsr_statistics(self, signal_id, start_sample_id, increment, level, data, data_length);
    }  // else, use sample data
    JLS_LOGD2("f32(signal_id=%d, start_id=%" PRIi64 ", incr=%" PRIi64 ", level=0, len=%" PRIi64 ")",
              (int) signal_id, start_sample_id, increment, data_length);

    ROE(f64_buf_alloc((size_t) increment, &self->f64_stats_buf));
    ROE(f64_buf_alloc((size_t) signal_def->samples_per_data, &self->f64_sample_buf));
    int64_t buf_offset = 0;
    uint8_t entry_size_bits = jls_datatype_parse_size(signal_def->data_type);
    if (entry_size_bits > 32) {
        JLS_LOGE("entry_size > 64 (float64 stats) not yet supported");
        return JLS_ERROR_UNSUPPORTED_FILE;
    }

    ROE(fsr_seek(self, signal_id, 0, start_sample_id));
    ROE(rd(self));
    struct jls_fsr_data_s * s = (struct jls_fsr_data_s *) self->payload.start;
    int64_t chunk_sample_id = s->header.timestamp;
    if (s->header.entry_size_bits != entry_size_bits) {
        JLS_LOGE("invalid data entry size: %d", (int) s->header.entry_size_bits);
        return JLS_ERROR_PARAMETER_INVALID;
    }
    jls_dt_buffer_to_f64(&s->data[0], signal_def->data_type, self->f64_sample_buf->start, signal_def->samples_per_data);
    double * src = &self->f64_sample_buf->start[0];
    double * src_end = &self->f64_sample_buf->start[s->header.entry_count];
    if (start_sample_id > chunk_sample_id) {
        src += start_sample_id - chunk_sample_id;
    }
    double v_mean = 0.0;
    double v_min = DBL_MAX;
    double v_max = -DBL_MAX;
    double v_var = 0.0;
    double mean_scale = 1.0 / increment;
    double var_scale = 1.0;
    if (increment > 1) {
        var_scale = 1.0 / (increment - 1.0);
    }
    double v;

    while (data_length > 0) {
        if (src >= src_end) {
            ROE(jls_raw_chunk_seek(self->raw, self->chunk_cur.hdr.item_next));
            ROE(rd(self));
            if (self->chunk_cur.hdr.tag != JLS_TAG_TRACK_FSR_DATA) {
                JLS_LOGW("unexpected chunk tag: %d", (int) self->chunk_cur.hdr.tag);
            }
            if (self->chunk_cur.hdr.chunk_meta != signal_id) {
                JLS_LOGW("unexpected chunk meta: %d", (int) self->chunk_cur.hdr.chunk_meta);
            }
            s = (struct jls_fsr_data_s *) self->payload.start;
            if (s->header.entry_size_bits != entry_size_bits) {
                JLS_LOGE("invalid data entry size: %d", (int) s->header.entry_size_bits);
                return JLS_ERROR_PARAMETER_INVALID;
            }
            chunk_sample_id = s->header.timestamp;
            jls_dt_buffer_to_f64(&s->data[0], signal_def->data_type, self->f64_sample_buf->start, signal_def->samples_per_data);
            src = &self->f64_sample_buf->start[0];
            src_end = &self->f64_sample_buf->start[s->header.entry_count];
        }
        v = *src++;
        v_mean += v;
        if (v < v_min) {
            v_min = v;
        }
        if (v > v_max) {
            v_max = v;
        }
        self->f64_stats_buf->start[buf_offset++] = v;

        if (buf_offset >= increment) {
            v_mean *= mean_scale;
            v_var = 0.0;
            for (int64_t i = 0; i < increment; ++i) {
                double v_diff = self->f64_stats_buf->start[i] - v_mean;
                v_var += v_diff * v_diff;
            }
            v_var *= var_scale;

            data[JLS_SUMMARY_FSR_MEAN] = v_mean;
            data[JLS_SUMMARY_FSR_MIN] = v_min;
            data[JLS_SUMMARY_FSR_MAX] = v_max;
            data[JLS_SUMMARY_FSR_STD] = sqrt(v_var);
            data += JLS_SUMMARY_FSR_COUNT;

            buf_offset = 0;
            v_mean = 0.0;
            v_min = DBL_MAX;
            v_max = -DBL_MAX;
            --data_length;
        }
    }
    return 0;
}

int32_t jls_rd_annotations(struct jls_rd_s * self, uint16_t signal_id, int64_t timestamp,
                           jls_rd_annotation_cbk_fn cbk_fn, void * cbk_user_data) {
    struct jls_annotation_s * annotation;
    if (!cbk_fn) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    if (!is_signal_defined(self, signal_id)) {
        return JLS_ERROR_NOT_FOUND;
    }

    const int64_t sample_id_offset = self->signal_def[signal_id].sample_id_offset;
    timestamp += sample_id_offset;

    int32_t rv = ts_seek(self, signal_id, 0, JLS_TRACK_TYPE_ANNOTATION, timestamp);
    if (rv == JLS_ERROR_NOT_FOUND) {
        return 0;  // no annotations, and that's just fine
    } else if (rv) {
        return rv;
    }

    // iterate
    int64_t pos = jls_raw_chunk_tell(self->raw);
    while (pos) {
        ROE(jls_raw_chunk_seek(self->raw, pos));
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag != JLS_TAG_TRACK_ANNOTATION_DATA) {
            return JLS_ERROR_NOT_FOUND;
        }
        annotation = (struct jls_annotation_s *) self->payload.start;
        annotation->timestamp -= sample_id_offset;
        if (cbk_fn(cbk_user_data, annotation)) {
            return 0;
        }
        pos = self->chunk_cur.hdr.item_next;
    }
    return 0;
}

int32_t jls_rd_user_data(struct jls_rd_s * self, jls_rd_user_data_cbk_fn cbk_fn, void * cbk_user_data) {
    int32_t rv;
    if (!cbk_fn) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    int64_t pos = self->user_data_head.hdr.item_next;
    uint16_t chunk_meta;
    while (pos) {
        ROE(jls_raw_chunk_seek(self->raw, pos));
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag != JLS_TAG_USER_DATA) {
            return JLS_ERROR_NOT_FOUND;
        }
        uint8_t storage_type = (uint8_t) ((self->chunk_cur.hdr.chunk_meta >> 12) & 0x0f);
        switch (storage_type) {
            case JLS_STORAGE_TYPE_BINARY:  // intentional fall-through
            case JLS_STORAGE_TYPE_STRING:  // intentional fall-through
            case JLS_STORAGE_TYPE_JSON:
                break;
            default:
                return JLS_ERROR_PARAMETER_INVALID;
        }
        chunk_meta = self->chunk_cur.hdr.chunk_meta & 0x0fff;
        rv = cbk_fn(cbk_user_data, chunk_meta, storage_type,
                    self->payload.start, self->chunk_cur.hdr.payload_length);
        if (rv) {  // iteration done
            return 0;
        }
        pos = self->chunk_cur.hdr.item_next;
    }
    return 0;
}

JLS_API int32_t jls_rd_utc(struct jls_rd_s * self, uint16_t signal_id, int64_t sample_id,
                           jls_rd_utc_cbk_fn cbk_fn, void * cbk_user_data) {
    struct jls_utc_summary_s * utc;
    if (!cbk_fn) {
        return JLS_ERROR_PARAMETER_INVALID;
    }
    if (!is_signal_defined(self, signal_id)) {
        return JLS_ERROR_NOT_FOUND;
    }

    const int64_t sample_id_offset = self->signal_def[signal_id].sample_id_offset;
    sample_id += sample_id_offset;
    int32_t rv = ts_seek(self, signal_id, 1, JLS_TRACK_TYPE_UTC, sample_id);
    if (rv == JLS_ERROR_NOT_FOUND) {
        return 0;  // no utc entries, and that's just fine
    } else if (rv) {
        return rv;
    }

    // iterate
    struct jls_chunk_header_s hdr;
    hdr.item_next = jls_raw_chunk_tell(self->raw);

    while (hdr.item_next) {
        ROE(jls_raw_chunk_seek(self->raw, hdr.item_next));
        ROE(jls_raw_rd_header(self->raw, &hdr));
        if (hdr.tag != JLS_TAG_TRACK_UTC_INDEX) {
            return JLS_ERROR_NOT_FOUND;
        }
        ROE(jls_raw_chunk_next(self->raw));
        ROE(rd(self));
        if (self->chunk_cur.hdr.tag != JLS_TAG_TRACK_UTC_SUMMARY) {
            return JLS_ERROR_NOT_FOUND;
        }
        utc = (struct jls_utc_summary_s *) self->payload.start;
        uint32_t idx = 0;
        for (; (idx < utc->header.entry_count) && (sample_id > utc->entries[idx].sample_id); ++idx) {
            // iterate
        }
        uint32_t size = utc->header.entry_count - idx;
        for (uint32_t entry_idx = idx; entry_idx < utc->header.entry_count; ++entry_idx) {
            utc->entries[entry_idx].sample_id -= sample_id_offset;
        }
        if (size) {
            if (cbk_fn(cbk_user_data, utc->entries + idx, size)) {
                return 0;
            }
        }
    }
    return 0;
}

static int32_t utc_load(struct jls_rd_s * self, uint16_t signal_id) {
    if (!is_signal_defined_type(self, signal_id, JLS_SIGNAL_TYPE_FSR)) {
        return JLS_ERROR_NOT_FOUND;
    }
    struct signal_s * signal = &self->signals[signal_id];
    if (NULL != signal->rd_fsr) {
        return 0;
    }
    signal->rd_fsr = jls_rd_fsr_alloc(self->signal_def[signal_id].sample_rate);
    if (NULL == signal->rd_fsr) {
        return JLS_ERROR_NOT_ENOUGH_MEMORY;
    }
    int64_t sample_rate = self->signal_def[signal_id].sample_rate;
    int64_t sample_start = -3600 * sample_rate;  // within the last hour
    return jls_rd_utc(self, signal_id, sample_start, jls_rd_fsr_add_cbk, signal->rd_fsr);
}

int32_t jls_rd_sample_id_to_timestamp(struct jls_rd_s * self, uint16_t signal_id,
                                      int64_t sample_id, int64_t * timestamp) {
    ROE(utc_load(self, signal_id));
    return jls_rd_fsr_sample_id_to_timestamp(self->signals[signal_id].rd_fsr, sample_id, timestamp);
}

int32_t jls_rd_timestamp_to_sample_id(struct jls_rd_s * self, uint16_t signal_id,
                                              int64_t timestamp, int64_t * sample_id) {
    ROE(utc_load(self, signal_id));
    return jls_rd_fsr_timestamp_to_sample_id(self->signals[signal_id].rd_fsr, timestamp, sample_id);
}
