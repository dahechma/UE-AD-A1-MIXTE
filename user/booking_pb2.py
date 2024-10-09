# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: booking.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'booking.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\rbooking.proto\x12\x07\x62ooking\"\x07\n\x05\x45mpty\"\x1f\n\rUserIdRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\"\x1b\n\x0b\x44\x61teRequest\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\"1\n\x11\x41\x64\x64\x42ookingRequest\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x02 \x01(\t\"(\n\x07\x42ooking\x12\x0e\n\x06userid\x18\x01 \x01(\t\x12\r\n\x05\x64\x61tes\x18\x02 \x03(\t\"6\n\x10\x42ookingsResponse\x12\"\n\x08\x62ookings\x18\x01 \x03(\x0b\x32\x10.booking.Booking\"4\n\x0f\x42ookingResponse\x12!\n\x07\x62ooking\x18\x01 \x01(\x0b\x32\x10.booking.Booking\"\x1e\n\rMovieResponse\x12\r\n\x05movie\x18\x01 \x01(\t\"%\n\x12\x41\x64\x64\x42ookingResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xa2\x02\n\x0e\x42ookingService\x12\x38\n\x0bGetBookings\x12\x0e.booking.Empty\x1a\x19.booking.BookingsResponse\x12G\n\x13GetBookingsByUserId\x12\x16.booking.UserIdRequest\x1a\x18.booking.BookingResponse\x12>\n\x0eGetMovieByDate\x12\x14.booking.DateRequest\x1a\x16.booking.MovieResponse\x12M\n\x12\x41\x64\x64\x42ookingByUserId\x12\x1a.booking.AddBookingRequest\x1a\x1b.booking.AddBookingResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'booking_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMPTY']._serialized_start=26
  _globals['_EMPTY']._serialized_end=33
  _globals['_USERIDREQUEST']._serialized_start=35
  _globals['_USERIDREQUEST']._serialized_end=66
  _globals['_DATEREQUEST']._serialized_start=68
  _globals['_DATEREQUEST']._serialized_end=95
  _globals['_ADDBOOKINGREQUEST']._serialized_start=97
  _globals['_ADDBOOKINGREQUEST']._serialized_end=146
  _globals['_BOOKING']._serialized_start=148
  _globals['_BOOKING']._serialized_end=188
  _globals['_BOOKINGSRESPONSE']._serialized_start=190
  _globals['_BOOKINGSRESPONSE']._serialized_end=244
  _globals['_BOOKINGRESPONSE']._serialized_start=246
  _globals['_BOOKINGRESPONSE']._serialized_end=298
  _globals['_MOVIERESPONSE']._serialized_start=300
  _globals['_MOVIERESPONSE']._serialized_end=330
  _globals['_ADDBOOKINGRESPONSE']._serialized_start=332
  _globals['_ADDBOOKINGRESPONSE']._serialized_end=369
  _globals['_BOOKINGSERVICE']._serialized_start=372
  _globals['_BOOKINGSERVICE']._serialized_end=662
# @@protoc_insertion_point(module_scope)