# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: aggregate.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import fennel.gen.schema_pb2 as schema__pb2
import fennel.gen.window_pb2 as window__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0f\x61ggregate.proto\x12\x16\x66\x65nnel.proto.aggregate\x1a\x0cschema.proto\x1a\x0cwindow.proto\"\xaa\x02\n\x04Spec\x12*\n\x03sum\x18\x01 \x01(\x0b\x32\x1b.fennel.proto.aggregate.SumH\x00\x12\x32\n\x07\x61verage\x18\x02 \x01(\x0b\x32\x1f.fennel.proto.aggregate.AverageH\x00\x12.\n\x05\x63ount\x18\x03 \x01(\x0b\x32\x1d.fennel.proto.aggregate.CountH\x00\x12/\n\x06last_k\x18\x04 \x01(\x0b\x32\x1d.fennel.proto.aggregate.LastKH\x00\x12*\n\x03min\x18\x05 \x01(\x0b\x32\x1b.fennel.proto.aggregate.MinH\x00\x12*\n\x03max\x18\x06 \x01(\x0b\x32\x1b.fennel.proto.aggregate.MaxH\x00\x42\t\n\x07variant\"h\n\x03Sum\x12&\n\x02of\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\"}\n\x07\x41verage\x12&\n\x02of\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\x12\x0f\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x01\"\x8a\x01\n\x05\x43ount\x12\x0c\n\x04name\x18\x01 \x01(\t\x12+\n\x06window\x18\x02 \x01(\x0b\x32\x1b.fennel.proto.window.Window\x12\x0e\n\x06unique\x18\x03 \x01(\x08\x12\x0e\n\x06\x61pprox\x18\x04 \x01(\x08\x12&\n\x02of\x18\x05 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\"\x88\x01\n\x05LastK\x12&\n\x02of\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\x12\r\n\x05limit\x18\x04 \x01(\r\x12\r\n\x05\x64\x65\x64up\x18\x05 \x01(\x08\"\x95\x01\n\x03Min\x12&\n\x02of\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\x12+\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x0b\x32\x1a.fennel.proto.schema.Value\"\x95\x01\n\x03Max\x12&\n\x02of\x18\x01 \x01(\x0b\x32\x1a.fennel.proto.schema.Field\x12\x0c\n\x04name\x18\x02 \x01(\t\x12+\n\x06window\x18\x03 \x01(\x0b\x32\x1b.fennel.proto.window.Window\x12+\n\x07\x64\x65\x66\x61ult\x18\x04 \x01(\x0b\x32\x1a.fennel.proto.schema.Valueb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'aggregate_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _SPEC._serialized_start=72
  _SPEC._serialized_end=370
  _SUM._serialized_start=372
  _SUM._serialized_end=476
  _AVERAGE._serialized_start=478
  _AVERAGE._serialized_end=603
  _COUNT._serialized_start=606
  _COUNT._serialized_end=744
  _LASTK._serialized_start=747
  _LASTK._serialized_end=883
  _MIN._serialized_start=886
  _MIN._serialized_end=1035
  _MAX._serialized_start=1038
  _MAX._serialized_end=1187
# @@protoc_insertion_point(module_scope)
