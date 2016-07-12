# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tensorflow/core/util/test_log.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tensorflow/core/util/test_log.proto',
  package='tensorflow',
  syntax='proto3',
  serialized_pb=_b('\n#tensorflow/core/util/test_log.proto\x12\ntensorflow\x1a\x19google/protobuf/any.proto\"D\n\nEntryValue\x12\x16\n\x0c\x64ouble_value\x18\x01 \x01(\x01H\x00\x12\x16\n\x0cstring_value\x18\x02 \x01(\tH\x00\x42\x06\n\x04kind\"\xe5\x01\n\x0e\x42\x65nchmarkEntry\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\r\n\x05iters\x18\x02 \x01(\x03\x12\x10\n\x08\x63pu_time\x18\x03 \x01(\x01\x12\x11\n\twall_time\x18\x04 \x01(\x01\x12\x12\n\nthroughput\x18\x05 \x01(\x01\x12\x36\n\x06\x65xtras\x18\x06 \x03(\x0b\x32&.tensorflow.BenchmarkEntry.ExtrasEntry\x1a\x45\n\x0b\x45xtrasEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.tensorflow.EntryValue:\x02\x38\x01\"=\n\x10\x42\x65nchmarkEntries\x12)\n\x05\x65ntry\x18\x01 \x03(\x0b\x32\x1a.tensorflow.BenchmarkEntry\"B\n\x12\x42uildConfiguration\x12\x0c\n\x04mode\x18\x01 \x01(\t\x12\x10\n\x08\x63\x63_flags\x18\x02 \x03(\t\x12\x0c\n\x04opts\x18\x03 \x03(\t\"J\n\x08\x43ommitId\x12\x14\n\nchangelist\x18\x01 \x01(\x03H\x00\x12\x0e\n\x04hash\x18\x02 \x01(\tH\x00\x12\x10\n\x08snapshot\x18\x03 \x01(\tB\x06\n\x04kind\"\xde\x01\n\x07\x43PUInfo\x12\x11\n\tnum_cores\x18\x01 \x01(\x03\x12\x19\n\x11num_cores_allowed\x18\x02 \x01(\x03\x12\x13\n\x0bmhz_per_cpu\x18\x03 \x01(\x01\x12\x10\n\x08\x63pu_info\x18\x04 \x01(\t\x12\x14\n\x0c\x63pu_governor\x18\x05 \x01(\t\x12\x36\n\ncache_size\x18\x06 \x03(\x0b\x32\".tensorflow.CPUInfo.CacheSizeEntry\x1a\x30\n\x0e\x43\x61\x63heSizeEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\".\n\nMemoryInfo\x12\r\n\x05total\x18\x01 \x01(\x03\x12\x11\n\tavailable\x18\x02 \x01(\x03\"6\n\x07GPUInfo\x12\r\n\x05model\x18\x01 \x01(\t\x12\x0c\n\x04uuid\x18\x02 \x01(\t\x12\x0e\n\x06\x62us_id\x18\x03 \x01(\t\"p\n\x0cPlatformInfo\x12\x0c\n\x04\x62its\x18\x01 \x01(\t\x12\x0f\n\x07linkage\x18\x02 \x01(\t\x12\x0f\n\x07machine\x18\x03 \x01(\t\x12\x0f\n\x07release\x18\x04 \x01(\t\x12\x0e\n\x06system\x18\x05 \x01(\t\x12\x0f\n\x07version\x18\x06 \x01(\t\"e\n\x13\x41vailableDeviceInfo\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04type\x18\x02 \x01(\t\x12\x14\n\x0cmemory_limit\x18\x03 \x01(\x03\x12\x1c\n\x14physical_description\x18\x04 \x01(\t\"\xb3\x02\n\x14MachineConfiguration\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x19\n\x11serial_identifier\x18\x07 \x01(\t\x12/\n\rplatform_info\x18\x02 \x01(\x0b\x32\x18.tensorflow.PlatformInfo\x12%\n\x08\x63pu_info\x18\x03 \x01(\x0b\x32\x13.tensorflow.CPUInfo\x12)\n\x0b\x64\x65vice_info\x18\x04 \x03(\x0b\x32\x14.google.protobuf.Any\x12>\n\x15\x61vailable_device_info\x18\x05 \x03(\x0b\x32\x1f.tensorflow.AvailableDeviceInfo\x12+\n\x0bmemory_info\x18\x06 \x01(\x0b\x32\x16.tensorflow.MemoryInfo\"$\n\x10RunConfiguration\x12\x10\n\x08\x61rgument\x18\x01 \x03(\t\"\xd2\x02\n\x0bTestResults\x12\x0e\n\x06target\x18\x01 \x01(\t\x12-\n\x07\x65ntries\x18\x02 \x01(\x0b\x32\x1c.tensorflow.BenchmarkEntries\x12;\n\x13\x62uild_configuration\x18\x03 \x01(\x0b\x32\x1e.tensorflow.BuildConfiguration\x12\'\n\tcommit_id\x18\x04 \x01(\x0b\x32\x14.tensorflow.CommitId\x12\x12\n\nstart_time\x18\x05 \x01(\x03\x12\x10\n\x08run_time\x18\x06 \x01(\x01\x12?\n\x15machine_configuration\x18\x07 \x01(\x0b\x32 .tensorflow.MachineConfiguration\x12\x37\n\x11run_configuration\x18\x08 \x01(\x0b\x32\x1c.tensorflow.RunConfigurationB.\n\x1borg.tensorflow.util.testlogB\rTestLogProtosP\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_ENTRYVALUE = _descriptor.Descriptor(
  name='EntryValue',
  full_name='tensorflow.EntryValue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='double_value', full_name='tensorflow.EntryValue.double_value', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='tensorflow.EntryValue.string_value', index=1,
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
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='kind', full_name='tensorflow.EntryValue.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=78,
  serialized_end=146,
)


_BENCHMARKENTRY_EXTRASENTRY = _descriptor.Descriptor(
  name='ExtrasEntry',
  full_name='tensorflow.BenchmarkEntry.ExtrasEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.BenchmarkEntry.ExtrasEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.BenchmarkEntry.ExtrasEntry.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=309,
  serialized_end=378,
)

_BENCHMARKENTRY = _descriptor.Descriptor(
  name='BenchmarkEntry',
  full_name='tensorflow.BenchmarkEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.BenchmarkEntry.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='iters', full_name='tensorflow.BenchmarkEntry.iters', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_time', full_name='tensorflow.BenchmarkEntry.cpu_time', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wall_time', full_name='tensorflow.BenchmarkEntry.wall_time', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='throughput', full_name='tensorflow.BenchmarkEntry.throughput', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='extras', full_name='tensorflow.BenchmarkEntry.extras', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_BENCHMARKENTRY_EXTRASENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=149,
  serialized_end=378,
)


_BENCHMARKENTRIES = _descriptor.Descriptor(
  name='BenchmarkEntries',
  full_name='tensorflow.BenchmarkEntries',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry', full_name='tensorflow.BenchmarkEntries.entry', index=0,
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
  serialized_start=380,
  serialized_end=441,
)


_BUILDCONFIGURATION = _descriptor.Descriptor(
  name='BuildConfiguration',
  full_name='tensorflow.BuildConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='mode', full_name='tensorflow.BuildConfiguration.mode', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cc_flags', full_name='tensorflow.BuildConfiguration.cc_flags', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='opts', full_name='tensorflow.BuildConfiguration.opts', index=2,
      number=3, type=9, cpp_type=9, label=3,
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
  serialized_start=443,
  serialized_end=509,
)


_COMMITID = _descriptor.Descriptor(
  name='CommitId',
  full_name='tensorflow.CommitId',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='changelist', full_name='tensorflow.CommitId.changelist', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hash', full_name='tensorflow.CommitId.hash', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='snapshot', full_name='tensorflow.CommitId.snapshot', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
    _descriptor.OneofDescriptor(
      name='kind', full_name='tensorflow.CommitId.kind',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=511,
  serialized_end=585,
)


_CPUINFO_CACHESIZEENTRY = _descriptor.Descriptor(
  name='CacheSizeEntry',
  full_name='tensorflow.CPUInfo.CacheSizeEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='tensorflow.CPUInfo.CacheSizeEntry.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='tensorflow.CPUInfo.CacheSizeEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=762,
  serialized_end=810,
)

_CPUINFO = _descriptor.Descriptor(
  name='CPUInfo',
  full_name='tensorflow.CPUInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num_cores', full_name='tensorflow.CPUInfo.num_cores', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_cores_allowed', full_name='tensorflow.CPUInfo.num_cores_allowed', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mhz_per_cpu', full_name='tensorflow.CPUInfo.mhz_per_cpu', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_info', full_name='tensorflow.CPUInfo.cpu_info', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_governor', full_name='tensorflow.CPUInfo.cpu_governor', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cache_size', full_name='tensorflow.CPUInfo.cache_size', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CPUINFO_CACHESIZEENTRY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=588,
  serialized_end=810,
)


_MEMORYINFO = _descriptor.Descriptor(
  name='MemoryInfo',
  full_name='tensorflow.MemoryInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='total', full_name='tensorflow.MemoryInfo.total', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='available', full_name='tensorflow.MemoryInfo.available', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=812,
  serialized_end=858,
)


_GPUINFO = _descriptor.Descriptor(
  name='GPUInfo',
  full_name='tensorflow.GPUInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='model', full_name='tensorflow.GPUInfo.model', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uuid', full_name='tensorflow.GPUInfo.uuid', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bus_id', full_name='tensorflow.GPUInfo.bus_id', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=860,
  serialized_end=914,
)


_PLATFORMINFO = _descriptor.Descriptor(
  name='PlatformInfo',
  full_name='tensorflow.PlatformInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bits', full_name='tensorflow.PlatformInfo.bits', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='linkage', full_name='tensorflow.PlatformInfo.linkage', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='machine', full_name='tensorflow.PlatformInfo.machine', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='release', full_name='tensorflow.PlatformInfo.release', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='system', full_name='tensorflow.PlatformInfo.system', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='version', full_name='tensorflow.PlatformInfo.version', index=5,
      number=6, type=9, cpp_type=9, label=1,
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
  serialized_start=916,
  serialized_end=1028,
)


_AVAILABLEDEVICEINFO = _descriptor.Descriptor(
  name='AvailableDeviceInfo',
  full_name='tensorflow.AvailableDeviceInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tensorflow.AvailableDeviceInfo.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='tensorflow.AvailableDeviceInfo.type', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_limit', full_name='tensorflow.AvailableDeviceInfo.memory_limit', index=2,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='physical_description', full_name='tensorflow.AvailableDeviceInfo.physical_description', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=1030,
  serialized_end=1131,
)


_MACHINECONFIGURATION = _descriptor.Descriptor(
  name='MachineConfiguration',
  full_name='tensorflow.MachineConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hostname', full_name='tensorflow.MachineConfiguration.hostname', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_identifier', full_name='tensorflow.MachineConfiguration.serial_identifier', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platform_info', full_name='tensorflow.MachineConfiguration.platform_info', index=2,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cpu_info', full_name='tensorflow.MachineConfiguration.cpu_info', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_info', full_name='tensorflow.MachineConfiguration.device_info', index=4,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='available_device_info', full_name='tensorflow.MachineConfiguration.available_device_info', index=5,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memory_info', full_name='tensorflow.MachineConfiguration.memory_info', index=6,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1134,
  serialized_end=1441,
)


_RUNCONFIGURATION = _descriptor.Descriptor(
  name='RunConfiguration',
  full_name='tensorflow.RunConfiguration',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='argument', full_name='tensorflow.RunConfiguration.argument', index=0,
      number=1, type=9, cpp_type=9, label=3,
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
  serialized_start=1443,
  serialized_end=1479,
)


_TESTRESULTS = _descriptor.Descriptor(
  name='TestResults',
  full_name='tensorflow.TestResults',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='target', full_name='tensorflow.TestResults.target', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='entries', full_name='tensorflow.TestResults.entries', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='build_configuration', full_name='tensorflow.TestResults.build_configuration', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='commit_id', full_name='tensorflow.TestResults.commit_id', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='tensorflow.TestResults.start_time', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run_time', full_name='tensorflow.TestResults.run_time', index=5,
      number=6, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='machine_configuration', full_name='tensorflow.TestResults.machine_configuration', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='run_configuration', full_name='tensorflow.TestResults.run_configuration', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=1482,
  serialized_end=1820,
)

_ENTRYVALUE.oneofs_by_name['kind'].fields.append(
  _ENTRYVALUE.fields_by_name['double_value'])
_ENTRYVALUE.fields_by_name['double_value'].containing_oneof = _ENTRYVALUE.oneofs_by_name['kind']
_ENTRYVALUE.oneofs_by_name['kind'].fields.append(
  _ENTRYVALUE.fields_by_name['string_value'])
_ENTRYVALUE.fields_by_name['string_value'].containing_oneof = _ENTRYVALUE.oneofs_by_name['kind']
_BENCHMARKENTRY_EXTRASENTRY.fields_by_name['value'].message_type = _ENTRYVALUE
_BENCHMARKENTRY_EXTRASENTRY.containing_type = _BENCHMARKENTRY
_BENCHMARKENTRY.fields_by_name['extras'].message_type = _BENCHMARKENTRY_EXTRASENTRY
_BENCHMARKENTRIES.fields_by_name['entry'].message_type = _BENCHMARKENTRY
_COMMITID.oneofs_by_name['kind'].fields.append(
  _COMMITID.fields_by_name['changelist'])
_COMMITID.fields_by_name['changelist'].containing_oneof = _COMMITID.oneofs_by_name['kind']
_COMMITID.oneofs_by_name['kind'].fields.append(
  _COMMITID.fields_by_name['hash'])
_COMMITID.fields_by_name['hash'].containing_oneof = _COMMITID.oneofs_by_name['kind']
_CPUINFO_CACHESIZEENTRY.containing_type = _CPUINFO
_CPUINFO.fields_by_name['cache_size'].message_type = _CPUINFO_CACHESIZEENTRY
_MACHINECONFIGURATION.fields_by_name['platform_info'].message_type = _PLATFORMINFO
_MACHINECONFIGURATION.fields_by_name['cpu_info'].message_type = _CPUINFO
_MACHINECONFIGURATION.fields_by_name['device_info'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_MACHINECONFIGURATION.fields_by_name['available_device_info'].message_type = _AVAILABLEDEVICEINFO
_MACHINECONFIGURATION.fields_by_name['memory_info'].message_type = _MEMORYINFO
_TESTRESULTS.fields_by_name['entries'].message_type = _BENCHMARKENTRIES
_TESTRESULTS.fields_by_name['build_configuration'].message_type = _BUILDCONFIGURATION
_TESTRESULTS.fields_by_name['commit_id'].message_type = _COMMITID
_TESTRESULTS.fields_by_name['machine_configuration'].message_type = _MACHINECONFIGURATION
_TESTRESULTS.fields_by_name['run_configuration'].message_type = _RUNCONFIGURATION
DESCRIPTOR.message_types_by_name['EntryValue'] = _ENTRYVALUE
DESCRIPTOR.message_types_by_name['BenchmarkEntry'] = _BENCHMARKENTRY
DESCRIPTOR.message_types_by_name['BenchmarkEntries'] = _BENCHMARKENTRIES
DESCRIPTOR.message_types_by_name['BuildConfiguration'] = _BUILDCONFIGURATION
DESCRIPTOR.message_types_by_name['CommitId'] = _COMMITID
DESCRIPTOR.message_types_by_name['CPUInfo'] = _CPUINFO
DESCRIPTOR.message_types_by_name['MemoryInfo'] = _MEMORYINFO
DESCRIPTOR.message_types_by_name['GPUInfo'] = _GPUINFO
DESCRIPTOR.message_types_by_name['PlatformInfo'] = _PLATFORMINFO
DESCRIPTOR.message_types_by_name['AvailableDeviceInfo'] = _AVAILABLEDEVICEINFO
DESCRIPTOR.message_types_by_name['MachineConfiguration'] = _MACHINECONFIGURATION
DESCRIPTOR.message_types_by_name['RunConfiguration'] = _RUNCONFIGURATION
DESCRIPTOR.message_types_by_name['TestResults'] = _TESTRESULTS

EntryValue = _reflection.GeneratedProtocolMessageType('EntryValue', (_message.Message,), dict(
  DESCRIPTOR = _ENTRYVALUE,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.EntryValue)
  ))
_sym_db.RegisterMessage(EntryValue)

BenchmarkEntry = _reflection.GeneratedProtocolMessageType('BenchmarkEntry', (_message.Message,), dict(

  ExtrasEntry = _reflection.GeneratedProtocolMessageType('ExtrasEntry', (_message.Message,), dict(
    DESCRIPTOR = _BENCHMARKENTRY_EXTRASENTRY,
    __module__ = 'tensorflow.core.util.test_log_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.BenchmarkEntry.ExtrasEntry)
    ))
  ,
  DESCRIPTOR = _BENCHMARKENTRY,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BenchmarkEntry)
  ))
_sym_db.RegisterMessage(BenchmarkEntry)
_sym_db.RegisterMessage(BenchmarkEntry.ExtrasEntry)

BenchmarkEntries = _reflection.GeneratedProtocolMessageType('BenchmarkEntries', (_message.Message,), dict(
  DESCRIPTOR = _BENCHMARKENTRIES,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BenchmarkEntries)
  ))
_sym_db.RegisterMessage(BenchmarkEntries)

BuildConfiguration = _reflection.GeneratedProtocolMessageType('BuildConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _BUILDCONFIGURATION,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.BuildConfiguration)
  ))
_sym_db.RegisterMessage(BuildConfiguration)

CommitId = _reflection.GeneratedProtocolMessageType('CommitId', (_message.Message,), dict(
  DESCRIPTOR = _COMMITID,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CommitId)
  ))
_sym_db.RegisterMessage(CommitId)

CPUInfo = _reflection.GeneratedProtocolMessageType('CPUInfo', (_message.Message,), dict(

  CacheSizeEntry = _reflection.GeneratedProtocolMessageType('CacheSizeEntry', (_message.Message,), dict(
    DESCRIPTOR = _CPUINFO_CACHESIZEENTRY,
    __module__ = 'tensorflow.core.util.test_log_pb2'
    # @@protoc_insertion_point(class_scope:tensorflow.CPUInfo.CacheSizeEntry)
    ))
  ,
  DESCRIPTOR = _CPUINFO,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.CPUInfo)
  ))
_sym_db.RegisterMessage(CPUInfo)
_sym_db.RegisterMessage(CPUInfo.CacheSizeEntry)

MemoryInfo = _reflection.GeneratedProtocolMessageType('MemoryInfo', (_message.Message,), dict(
  DESCRIPTOR = _MEMORYINFO,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MemoryInfo)
  ))
_sym_db.RegisterMessage(MemoryInfo)

GPUInfo = _reflection.GeneratedProtocolMessageType('GPUInfo', (_message.Message,), dict(
  DESCRIPTOR = _GPUINFO,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.GPUInfo)
  ))
_sym_db.RegisterMessage(GPUInfo)

PlatformInfo = _reflection.GeneratedProtocolMessageType('PlatformInfo', (_message.Message,), dict(
  DESCRIPTOR = _PLATFORMINFO,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.PlatformInfo)
  ))
_sym_db.RegisterMessage(PlatformInfo)

AvailableDeviceInfo = _reflection.GeneratedProtocolMessageType('AvailableDeviceInfo', (_message.Message,), dict(
  DESCRIPTOR = _AVAILABLEDEVICEINFO,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.AvailableDeviceInfo)
  ))
_sym_db.RegisterMessage(AvailableDeviceInfo)

MachineConfiguration = _reflection.GeneratedProtocolMessageType('MachineConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _MACHINECONFIGURATION,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.MachineConfiguration)
  ))
_sym_db.RegisterMessage(MachineConfiguration)

RunConfiguration = _reflection.GeneratedProtocolMessageType('RunConfiguration', (_message.Message,), dict(
  DESCRIPTOR = _RUNCONFIGURATION,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.RunConfiguration)
  ))
_sym_db.RegisterMessage(RunConfiguration)

TestResults = _reflection.GeneratedProtocolMessageType('TestResults', (_message.Message,), dict(
  DESCRIPTOR = _TESTRESULTS,
  __module__ = 'tensorflow.core.util.test_log_pb2'
  # @@protoc_insertion_point(class_scope:tensorflow.TestResults)
  ))
_sym_db.RegisterMessage(TestResults)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\033org.tensorflow.util.testlogB\rTestLogProtosP\001'))
_BENCHMARKENTRY_EXTRASENTRY.has_options = True
_BENCHMARKENTRY_EXTRASENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
_CPUINFO_CACHESIZEENTRY.has_options = True
_CPUINFO_CACHESIZEENTRY._options = _descriptor._ParseOptions(descriptor_pb2.MessageOptions(), _b('8\001'))
# @@protoc_insertion_point(module_scope)
