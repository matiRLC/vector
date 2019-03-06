# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: anki_vector/messaging/settings.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from anki_vector.messaging import messages_pb2 as anki__vector_dot_messaging_dot_messages__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='anki_vector/messaging/settings.proto',
  package='Anki.Vector.external_interface',
  syntax='proto3',
  serialized_pb=_b('\n$anki_vector/messaging/settings.proto\x12\x1e\x41nki.Vector.external_interface\x1a$anki_vector/messaging/messages.proto*%\n\nApiVersion\x12\x0b\n\x07INVALID\x10\x00\x12\n\n\x06LATEST\x10\x01*R\n\x06Volume\x12\x08\n\x04MUTE\x10\x00\x12\x07\n\x03LOW\x10\x01\x12\x0e\n\nMEDIUM_LOW\x10\x02\x12\n\n\x06MEDIUM\x10\x03\x12\x0f\n\x0bMEDIUM_HIGH\x10\x04\x12\x08\n\x04HIGH\x10\x05\x62\x06proto3')
  ,
  dependencies=[anki__vector_dot_messaging_dot_messages__pb2.DESCRIPTOR,])

_APIVERSION = _descriptor.EnumDescriptor(
  name='ApiVersion',
  full_name='Anki.Vector.external_interface.ApiVersion',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INVALID', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LATEST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=110,
  serialized_end=147,
)
_sym_db.RegisterEnumDescriptor(_APIVERSION)

ApiVersion = enum_type_wrapper.EnumTypeWrapper(_APIVERSION)
_VOLUME = _descriptor.EnumDescriptor(
  name='Volume',
  full_name='Anki.Vector.external_interface.Volume',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MUTE', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOW', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM_LOW', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MEDIUM_HIGH', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='HIGH', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=149,
  serialized_end=231,
)
_sym_db.RegisterEnumDescriptor(_VOLUME)

Volume = enum_type_wrapper.EnumTypeWrapper(_VOLUME)
INVALID = 0
LATEST = 1
MUTE = 0
LOW = 1
MEDIUM_LOW = 2
MEDIUM = 3
MEDIUM_HIGH = 4
HIGH = 5


DESCRIPTOR.enum_types_by_name['ApiVersion'] = _APIVERSION
DESCRIPTOR.enum_types_by_name['Volume'] = _VOLUME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)