# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: xrescode_extensions_v3.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='xrescode_extensions_v3.proto',
  package='xrescode',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1cxrescode_extensions_v3.proto\x12\x08xrescode\x1a google/protobuf/descriptor.proto\"\x90\x01\n\x0exrescode_index\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0e\n\x06\x66ields\x18\x02 \x03(\t\x12\x31\n\nindex_type\x18\x03 \x01(\x0e\x32\x1d.xrescode.xrescode_index_type\x12\x14\n\x0c\x66ile_mapping\x18\x04 \x01(\t\x12\x17\n\x0f\x61llow_not_found\x18\x05 \x01(\x08*Y\n\x13xrescode_index_type\x12\x0f\n\x0b\x45N_INDEX_KV\x10\x00\x12\x0f\n\x0b\x45N_INDEX_KL\x10\x01\x12\x0f\n\x0b\x45N_INDEX_IV\x10\x02\x12\x0f\n\x0b\x45N_INDEX_IL\x10\x03:3\n\tfile_list\x12\x1f.google.protobuf.MessageOptions\x18\xc7\n \x01(\t:3\n\tfile_path\x12\x1f.google.protobuf.MessageOptions\x18\xc8\n \x01(\t:K\n\x07indexes\x12\x1f.google.protobuf.MessageOptions\x18\xc9\n \x03(\x0b\x32\x18.xrescode.xrescode_index:.\n\x04tags\x12\x1f.google.protobuf.MessageOptions\x18\xca\n \x03(\t:4\n\nclass_name\x12\x1f.google.protobuf.MessageOptions\x18\xcb\n \x01(\t:1\n\texcel_row\x12\x1d.google.protobuf.FieldOptions\x18\xc7\n \x01(\x08\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR,])

_XRESCODE_INDEX_TYPE = _descriptor.EnumDescriptor(
  name='xrescode_index_type',
  full_name='xrescode.xrescode_index_type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='EN_INDEX_KV', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EN_INDEX_KL', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EN_INDEX_IV', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EN_INDEX_IL', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=223,
  serialized_end=312,
)
_sym_db.RegisterEnumDescriptor(_XRESCODE_INDEX_TYPE)

xrescode_index_type = enum_type_wrapper.EnumTypeWrapper(_XRESCODE_INDEX_TYPE)
EN_INDEX_KV = 0
EN_INDEX_KL = 1
EN_INDEX_IV = 2
EN_INDEX_IL = 3

FILE_LIST_FIELD_NUMBER = 1351
file_list = _descriptor.FieldDescriptor(
  name='file_list', full_name='xrescode.file_list', index=0,
  number=1351, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
FILE_PATH_FIELD_NUMBER = 1352
file_path = _descriptor.FieldDescriptor(
  name='file_path', full_name='xrescode.file_path', index=1,
  number=1352, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
INDEXES_FIELD_NUMBER = 1353
indexes = _descriptor.FieldDescriptor(
  name='indexes', full_name='xrescode.indexes', index=2,
  number=1353, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
TAGS_FIELD_NUMBER = 1354
tags = _descriptor.FieldDescriptor(
  name='tags', full_name='xrescode.tags', index=3,
  number=1354, type=9, cpp_type=9, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
CLASS_NAME_FIELD_NUMBER = 1355
class_name = _descriptor.FieldDescriptor(
  name='class_name', full_name='xrescode.class_name', index=4,
  number=1355, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=_b("").decode('utf-8'),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)
EXCEL_ROW_FIELD_NUMBER = 1351
excel_row = _descriptor.FieldDescriptor(
  name='excel_row', full_name='xrescode.excel_row', index=5,
  number=1351, type=8, cpp_type=7, label=1,
  has_default_value=False, default_value=False,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  serialized_options=None, file=DESCRIPTOR)


_XRESCODE_INDEX = _descriptor.Descriptor(
  name='xrescode_index',
  full_name='xrescode.xrescode_index',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='xrescode.xrescode_index.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fields', full_name='xrescode.xrescode_index.fields', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='index_type', full_name='xrescode.xrescode_index.index_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='file_mapping', full_name='xrescode.xrescode_index.file_mapping', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='allow_not_found', full_name='xrescode.xrescode_index.allow_not_found', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=221,
)

_XRESCODE_INDEX.fields_by_name['index_type'].enum_type = _XRESCODE_INDEX_TYPE
DESCRIPTOR.message_types_by_name['xrescode_index'] = _XRESCODE_INDEX
DESCRIPTOR.enum_types_by_name['xrescode_index_type'] = _XRESCODE_INDEX_TYPE
DESCRIPTOR.extensions_by_name['file_list'] = file_list
DESCRIPTOR.extensions_by_name['file_path'] = file_path
DESCRIPTOR.extensions_by_name['indexes'] = indexes
DESCRIPTOR.extensions_by_name['tags'] = tags
DESCRIPTOR.extensions_by_name['class_name'] = class_name
DESCRIPTOR.extensions_by_name['excel_row'] = excel_row
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

xrescode_index = _reflection.GeneratedProtocolMessageType('xrescode_index', (_message.Message,), {
  'DESCRIPTOR' : _XRESCODE_INDEX,
  '__module__' : 'xrescode_extensions_v3_pb2'
  # @@protoc_insertion_point(class_scope:xrescode.xrescode_index)
  })
_sym_db.RegisterMessage(xrescode_index)

google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(file_list)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(file_path)
indexes.message_type = _XRESCODE_INDEX
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(indexes)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(tags)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(class_name)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(excel_row)

# @@protoc_insertion_point(module_scope)
