# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: camera.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import wilson.proto.vector_pb2 as vector__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0c\x63\x61mera.proto\x12\x06wilson\x1a\x0cvector.proto\"J\n\x06\x43\x61mera\x12 \n\x08position\x18\x01 \x01(\x0b\x32\x0e.wilson.Vector\x12\x1e\n\x06target\x18\x02 \x01(\x0b\x32\x0e.wilson.Vectorb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'camera_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CAMERA._serialized_start=38
  _CAMERA._serialized_end=112
# @@protoc_insertion_point(module_scope)
