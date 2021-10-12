# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cvcio/classification/accounts.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from internal.google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2
from internal.cvcio.common import meta_pb2 as cvcio_dot_common_dot_meta__pb2
from internal.cvcio.common import predictions_pb2 as cvcio_dot_common_dot_predictions__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='cvcio/classification/accounts.proto',
  package='classification',
  syntax='proto3',
  serialized_options=b'Z+github.com/cvcio/proto/cvcio/classification',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n#cvcio/classification/accounts.proto\x12\x0e\x63lassification\x1a\x1cgoogle/api/annotations.proto\x1a\x17\x63vcio/common/meta.proto\x1a\x1e\x63vcio/common/predictions.proto\"\xce\x01\n\x0eTwitterAccount\x12\x11\n\tfollowers\x18\x01 \x01(\x03\x12\x0f\n\x07\x66riends\x18\x02 \x01(\x03\x12\x10\n\x08statuses\x18\x03 \x01(\x03\x12\x11\n\tfavorites\x18\x04 \x01(\x03\x12\r\n\x05lists\x18\x05 \x01(\x03\x12\x0b\n\x03\x66\x66r\x18\x06 \x01(\x01\x12\x0c\n\x04stfv\x18\x07 \x01(\x01\x12\r\n\x05\x66stfv\x18\x08 \x01(\x01\x12\r\n\x05\x64\x61tes\x18\t \x01(\x01\x12\x0f\n\x07\x61\x63tions\x18\n \x01(\x01\x12\x1a\n\x04meta\x18\x0b \x01(\x0b\x32\x0c.common.Meta\":\n\x0fResponseAccount\x12\'\n\x0bpredictions\x18\x01 \x03(\x0b\x32\x12.common.Prediction*h\n\x0c\x41\x63\x63ountClass\x12\x10\n\x0cROLE_UNKNOWN\x10\x00\x12\x0f\n\x0bROLE_ACTIVE\x10\x01\x12\x13\n\x0fROLE_INFLUENCER\x10\x02\x12\x0c\n\x08ROLE_NEW\x10\x03\x12\x12\n\x0eROLE_AMPLIFIER\x10\x04\x32\x8a\x01\n\x0e\x41\x63\x63ountService\x12x\n\x14\x44\x65tectTwitterAccount\x12\x1e.classification.TwitterAccount\x1a\x1f.classification.ResponseAccount\"\x1f\x82\xd3\xe4\x93\x02\x19\"\x14/v3/accounts/twitter:\x01*B-Z+github.com/cvcio/proto/cvcio/classificationb\x06proto3'
  ,
  dependencies=[google_dot_api_dot_annotations__pb2.DESCRIPTOR,cvcio_dot_common_dot_meta__pb2.DESCRIPTOR,cvcio_dot_common_dot_predictions__pb2.DESCRIPTOR,])

_ACCOUNTCLASS = _descriptor.EnumDescriptor(
  name='AccountClass',
  full_name='classification.AccountClass',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ROLE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROLE_ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROLE_INFLUENCER', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROLE_NEW', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ROLE_AMPLIFIER', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=411,
  serialized_end=515,
)
_sym_db.RegisterEnumDescriptor(_ACCOUNTCLASS)

AccountClass = enum_type_wrapper.EnumTypeWrapper(_ACCOUNTCLASS)
ROLE_UNKNOWN = 0
ROLE_ACTIVE = 1
ROLE_INFLUENCER = 2
ROLE_NEW = 3
ROLE_AMPLIFIER = 4



_TWITTERACCOUNT = _descriptor.Descriptor(
  name='TwitterAccount',
  full_name='classification.TwitterAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='followers', full_name='classification.TwitterAccount.followers', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='friends', full_name='classification.TwitterAccount.friends', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='statuses', full_name='classification.TwitterAccount.statuses', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='favorites', full_name='classification.TwitterAccount.favorites', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lists', full_name='classification.TwitterAccount.lists', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ffr', full_name='classification.TwitterAccount.ffr', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='stfv', full_name='classification.TwitterAccount.stfv', index=6,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fstfv', full_name='classification.TwitterAccount.fstfv', index=7,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='dates', full_name='classification.TwitterAccount.dates', index=8,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='actions', full_name='classification.TwitterAccount.actions', index=9,
      number=10, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='meta', full_name='classification.TwitterAccount.meta', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=143,
  serialized_end=349,
)


_RESPONSEACCOUNT = _descriptor.Descriptor(
  name='ResponseAccount',
  full_name='classification.ResponseAccount',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='predictions', full_name='classification.ResponseAccount.predictions', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=351,
  serialized_end=409,
)

_TWITTERACCOUNT.fields_by_name['meta'].message_type = cvcio_dot_common_dot_meta__pb2._META
_RESPONSEACCOUNT.fields_by_name['predictions'].message_type = cvcio_dot_common_dot_predictions__pb2._PREDICTION
DESCRIPTOR.message_types_by_name['TwitterAccount'] = _TWITTERACCOUNT
DESCRIPTOR.message_types_by_name['ResponseAccount'] = _RESPONSEACCOUNT
DESCRIPTOR.enum_types_by_name['AccountClass'] = _ACCOUNTCLASS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TwitterAccount = _reflection.GeneratedProtocolMessageType('TwitterAccount', (_message.Message,), {
  'DESCRIPTOR' : _TWITTERACCOUNT,
  '__module__' : 'cvcio.classification.accounts_pb2'
  # @@protoc_insertion_point(class_scope:classification.TwitterAccount)
  })
_sym_db.RegisterMessage(TwitterAccount)

ResponseAccount = _reflection.GeneratedProtocolMessageType('ResponseAccount', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSEACCOUNT,
  '__module__' : 'cvcio.classification.accounts_pb2'
  # @@protoc_insertion_point(class_scope:classification.ResponseAccount)
  })
_sym_db.RegisterMessage(ResponseAccount)


DESCRIPTOR._options = None

_ACCOUNTSERVICE = _descriptor.ServiceDescriptor(
  name='AccountService',
  full_name='classification.AccountService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=518,
  serialized_end=656,
  methods=[
  _descriptor.MethodDescriptor(
    name='DetectTwitterAccount',
    full_name='classification.AccountService.DetectTwitterAccount',
    index=0,
    containing_service=None,
    input_type=_TWITTERACCOUNT,
    output_type=_RESPONSEACCOUNT,
    serialized_options=b'\202\323\344\223\002\031\"\024/v3/accounts/twitter:\001*',
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_ACCOUNTSERVICE)

DESCRIPTOR.services_by_name['AccountService'] = _ACCOUNTSERVICE

# @@protoc_insertion_point(module_scope)
