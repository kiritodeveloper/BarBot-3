/* Automatically generated nanopb constant definitions */
/* Generated by nanopb-0.3.8 at Tue May  2 20:42:19 2017. */

#include "dwdistance.pb.h"

/* @@protoc_insertion_point(includes) */
#if PB_PROTO_HEADER_VERSION != 30
#error Regenerate this file with the current version of nanopb generator.
#endif



const pb_field_t DwDistance_fields[5] = {
    PB_FIELD(  2, UINT32  , SINGULAR, STATIC  , FIRST, DwDistance, send_id, send_id, 0),
    PB_FIELD(  3, UINT32  , SINGULAR, STATIC  , OTHER, DwDistance, recv_id, send_id, 0),
    PB_FIELD(  4, DOUBLE  , SINGULAR, STATIC  , OTHER, DwDistance, dist, recv_id, 0),
    PB_FIELD(  5, BOOL    , SINGULAR, STATIC  , OTHER, DwDistance, beacon, dist, 0),
    PB_LAST_FIELD
};


/* On some platforms (such as AVR), double is really float.
 * These are not directly supported by nanopb, but see example_avr_double.
 * To get rid of this error, remove any double fields from your .proto.
 */
PB_STATIC_ASSERT(sizeof(double) == 8, DOUBLE_MUST_BE_8_BYTES)

/* @@protoc_insertion_point(eof) */
