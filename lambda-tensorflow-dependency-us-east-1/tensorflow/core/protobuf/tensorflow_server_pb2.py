# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/protobuf/tensorflow_server.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tensorflow.core.protobuf import config_pb2 as tensorflow_dot_core_dot_protobuf_dot_config__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/protobuf/tensorflow_server.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n0tensorflow/core/protobuf/tensorflow_server.proto\x12\ntensorflow\x1a%tensorflow/core/protobuf/config.proto\"r\n\x06JobDef\x12\x0c\n\x04name\x18\x01 \x01(\t\x12,\n\x05tasks\x18\x02 \x03(\x0b\x32\x1d.tensorflow.JobDef.TasksEntry\x1a,\n\nTasksEntry\x12\x0b\n\x03key\x18\x01 \x01(\x05\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"-\n\nClusterDef\x12\x1f\n\x03job\x18\x01 \x03(\x0b\x32\x12.tensorflow.JobDef\"\xa5\x01\n\tServerDef\x12\'\n\x07\x63luster\x18\x01 \x01(\x0b\x32\x16.tensorflow.ClusterDef\x12\x10\n\x08job_name\x18\x02 \x01(\t\x12\x12\n\ntask_index\x18\x03 \x01(\x05\x12\x37\n\x16\x64\x65\x66\x61ult_session_config\x18\x04 \x01(\x0b\x32\x17.tensorflow.ConfigProto\x12\x10\n\x08protocol\x18\x05 \x01(\tB,\n\x1aorg.tensorflow.distruntimeB\x0cServerProtosP\x01\x62\x06proto3')
  ,
  dependencies=[tensorflow_dot_core_dot_protobuf_dot_config__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_JOBDEF_TASKSENTRY = _descriptor.Descriptor(
  name='TasksEntry',
  full_name='tensorflow.JobDef.TasksEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.JobDef.TasksEntry.key', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.JobDef.TasksEntry.value', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=_descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001')),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=173,
  serialized_end=217,
)

_JOBDEF = _descriptor.Descriptor(
  name='JobDef',
  full_name='tensorflow.JobDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.JobDef.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tasks', full_name='tensorflow.JobDef.tasks', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_JOBDEF_TASKSENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=103,
  serialized_end=217,
)


_CLUSTERDEF = _descriptor.Descriptor(
  name='ClusterDef',
  full_name='tensorflow.ClusterDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='job', full_name='tensorflow.ClusterDef.job', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=219,
  serialized_end=264,
)


_SERVERDEF = _descriptor.Descriptor(
  name='ServerDef',
  full_name='tensorflow.ServerDef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cluster', full_name='tensorflow.ServerDef.cluster', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='job_name', full_name='tensorflow.ServerDef.job_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='task_index', full_name='tensorflow.ServerDef.task_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='default_session_config', full_name='tensorflow.ServerDef.default_session_config', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='protocol', full_name='tensorflow.ServerDef.protocol', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=267,
  serialized_end=432,
)

_JOBDEF_TASKSENTRY.containing_type = _JOBDEF
_JOBDEF.fields_by_name['tasks'].message_type = _JOBDEF_TASKSENTRY
_CLUSTERDEF.fields_by_name['job'].message_type = _JOBDEF
_SERVERDEF.fields_by_name['cluster'].message_type = _CLUSTERDEF
_SERVERDEF.fields_by_name['default_session_config'].message_type = tensorflow_dot_core_dot_protobuf_dot_config__pb2._CONFIGPROTO
DESCRIPTOR.message_types_by_name['JobDef'] = _JOBDEF
DESCRIPTOR.message_types_by_name['ClusterDef'] = _CLUSTERDEF
DESCRIPTOR.message_types_by_name['ServerDef'] = _SERVERDEF

JobDef = _reflection.GeneratedProtocolMessageType('JobDef', (_message.Message,), dict(

  TasksEntry = _reflection.GeneratedProtocolMessageType('TasksEntry', (_message.Message,), dict(
    DESCRIPTOR = _JOBDEF_TASKSENTRY,
    __module__ = 'tensorflow.core.protobuf.tensorflow_server_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.JobDef.TasksEntry)
    ))
  ,
  DESCRIPTOR = _JOBDEF,
  __module__ = 'tensorflow.core.protobuf.tensorflow_server_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.JobDef)
  ))
_sym_db.RegisterMessage(JobDef)
_sym_db.RegisterMessage(JobDef.TasksEntry)

ClusterDef = _reflection.GeneratedProtocolMessageType('ClusterDef', (_message.Message,), dict(
  DESCRIPTOR = _CLUSTERDEF,
  __module__ = 'tensorflow.core.protobuf.tensorflow_server_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ClusterDef)
  ))
_sym_db.RegisterMessage(ClusterDef)

ServerDef = _reflection.GeneratedProtocolMessageType('ServerDef', (_message.Message,), dict(
  DESCRIPTOR = _SERVERDEF,
  __module__ = 'tensorflow.core.protobuf.tensorflow_server_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.ServerDef)
  ))
_sym_db.RegisterMessage(ServerDef)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\032org.tensorflow.distruntimeB\014ServerProtosP\001'))
_JOBDEF_TASKSENTRY.has_options = True
_JOBDEF_TASKSENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
