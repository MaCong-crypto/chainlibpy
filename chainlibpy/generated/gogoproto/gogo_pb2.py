
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='gogoproto/gogo.proto', package='gogoproto', syntax='proto2', serialized_options=b'\n\x13com.google.protobufB\nGoGoProtosZ"github.com/gogo/protobuf/gogoproto', create_key=_descriptor._internal_create_key, serialized_pb=b'\n\x14gogoproto/gogo.proto\x12\tgogoproto\x1a google/protobuf/descriptor.proto:;\n\x13goproto_enum_prefix\x12\x1c.google.protobuf.EnumOptions\x18\xb1\xe4\x03 \x01(\x08:=\n\x15goproto_enum_stringer\x12\x1c.google.protobuf.EnumOptions\x18\xc5\xe4\x03 \x01(\x08:5\n\renum_stringer\x12\x1c.google.protobuf.EnumOptions\x18\xc6\xe4\x03 \x01(\x08:7\n\x0fenum_customname\x12\x1c.google.protobuf.EnumOptions\x18\xc7\xe4\x03 \x01(\t:0\n\x08enumdecl\x12\x1c.google.protobuf.EnumOptions\x18\xc8\xe4\x03 \x01(\x08:A\n\x14enumvalue_customname\x12!.google.protobuf.EnumValueOptions\x18\xd1\x83\x04 \x01(\t:;\n\x13goproto_getters_all\x12\x1c.google.protobuf.FileOptions\x18\x99\xec\x03 \x01(\x08:?\n\x17goproto_enum_prefix_all\x12\x1c.google.protobuf.FileOptions\x18\x9a\xec\x03 \x01(\x08:<\n\x14goproto_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\x9b\xec\x03 \x01(\x08:9\n\x11verbose_equal_all\x12\x1c.google.protobuf.FileOptions\x18\x9c\xec\x03 \x01(\x08:0\n\x08face_all\x12\x1c.google.protobuf.FileOptions\x18\x9d\xec\x03 \x01(\x08:4\n\x0cgostring_all\x12\x1c.google.protobuf.FileOptions\x18\x9e\xec\x03 \x01(\x08:4\n\x0cpopulate_all\x12\x1c.google.protobuf.FileOptions\x18\x9f\xec\x03 \x01(\x08:4\n\x0cstringer_all\x12\x1c.google.protobuf.FileOptions\x18\xa0\xec\x03 \x01(\x08:3\n\x0bonlyone_all\x12\x1c.google.protobuf.FileOptions\x18\xa1\xec\x03 \x01(\x08:1\n\tequal_all\x12\x1c.google.protobuf.FileOptions\x18\xa5\xec\x03 \x01(\x08:7\n\x0fdescription_all\x12\x1c.google.protobuf.FileOptions\x18\xa6\xec\x03 \x01(\x08:3\n\x0btestgen_all\x12\x1c.google.protobuf.FileOptions\x18\xa7\xec\x03 \x01(\x08:4\n\x0cbenchgen_all\x12\x1c.google.protobuf.FileOptions\x18\xa8\xec\x03 \x01(\x08:5\n\rmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xa9\xec\x03 \x01(\x08:7\n\x0funmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xaa\xec\x03 \x01(\x08:<\n\x14stable_marshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xab\xec\x03 \x01(\x08:1\n\tsizer_all\x12\x1c.google.protobuf.FileOptions\x18\xac\xec\x03 \x01(\x08:A\n\x19goproto_enum_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\xad\xec\x03 \x01(\x08:9\n\x11enum_stringer_all\x12\x1c.google.protobuf.FileOptions\x18\xae\xec\x03 \x01(\x08:<\n\x14unsafe_marshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xaf\xec\x03 \x01(\x08:>\n\x16unsafe_unmarshaler_all\x12\x1c.google.protobuf.FileOptions\x18\xb0\xec\x03 \x01(\x08:B\n\x1agoproto_extensions_map_all\x12\x1c.google.protobuf.FileOptions\x18\xb1\xec\x03 \x01(\x08:@\n\x18goproto_unrecognized_all\x12\x1c.google.protobuf.FileOptions\x18\xb2\xec\x03 \x01(\x08:8\n\x10gogoproto_import\x12\x1c.google.protobuf.FileOptions\x18\xb3\xec\x03 \x01(\x08:6\n\x0eprotosizer_all\x12\x1c.google.protobuf.FileOptions\x18\xb4\xec\x03 \x01(\x08:3\n\x0bcompare_all\x12\x1c.google.protobuf.FileOptions\x18\xb5\xec\x03 \x01(\x08:4\n\x0ctypedecl_all\x12\x1c.google.protobuf.FileOptions\x18\xb6\xec\x03 \x01(\x08:4\n\x0cenumdecl_all\x12\x1c.google.protobuf.FileOptions\x18\xb7\xec\x03 \x01(\x08:<\n\x14goproto_registration\x12\x1c.google.protobuf.FileOptions\x18\xb8\xec\x03 \x01(\x08:7\n\x0fmessagename_all\x12\x1c.google.protobuf.FileOptions\x18\xb9\xec\x03 \x01(\x08:=\n\x15goproto_sizecache_all\x12\x1c.google.protobuf.FileOptions\x18\xba\xec\x03 \x01(\x08:;\n\x13goproto_unkeyed_all\x12\x1c.google.protobuf.FileOptions\x18\xbb\xec\x03 \x01(\x08::\n\x0fgoproto_getters\x12\x1f.google.protobuf.MessageOptions\x18\x81\xf4\x03 \x01(\x08:;\n\x10goproto_stringer\x12\x1f.google.protobuf.MessageOptions\x18\x83\xf4\x03 \x01(\x08:8\n\rverbose_equal\x12\x1f.google.protobuf.MessageOptions\x18\x84\xf4\x03 \x01(\x08:/\n\x04face\x12\x1f.google.protobuf.MessageOptions\x18\x85\xf4\x03 \x01(\x08:3\n\x08gostring\x12\x1f.google.protobuf.MessageOptions\x18\x86\xf4\x03 \x01(\x08:3\n\x08populate\x12\x1f.google.protobuf.MessageOptions\x18\x87\xf4\x03 \x01(\x08:3\n\x08stringer\x12\x1f.google.protobuf.MessageOptions\x18\xc0\x8b\x04 \x01(\x08:2\n\x07onlyone\x12\x1f.google.protobuf.MessageOptions\x18\x89\xf4\x03 \x01(\x08:0\n\x05equal\x12\x1f.google.protobuf.MessageOptions\x18\x8d\xf4\x03 \x01(\x08:6\n\x0bdescription\x12\x1f.google.protobuf.MessageOptions\x18\x8e\xf4\x03 \x01(\x08:2\n\x07testgen\x12\x1f.google.protobuf.MessageOptions\x18\x8f\xf4\x03 \x01(\x08:3\n\x08benchgen\x12\x1f.google.protobuf.MessageOptions\x18\x90\xf4\x03 \x01(\x08:4\n\tmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x91\xf4\x03 \x01(\x08:6\n\x0bunmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x92\xf4\x03 \x01(\x08:;\n\x10stable_marshaler\x12\x1f.google.protobuf.MessageOptions\x18\x93\xf4\x03 \x01(\x08:0\n\x05sizer\x12\x1f.google.protobuf.MessageOptions\x18\x94\xf4\x03 \x01(\x08:;\n\x10unsafe_marshaler\x12\x1f.google.protobuf.MessageOptions\x18\x97\xf4\x03 \x01(\x08:=\n\x12unsafe_unmarshaler\x12\x1f.google.protobuf.MessageOptions\x18\x98\xf4\x03 \x01(\x08:A\n\x16goproto_extensions_map\x12\x1f.google.protobuf.MessageOptions\x18\x99\xf4\x03 \x01(\x08:?\n\x14goproto_unrecognized\x12\x1f.google.protobuf.MessageOptions\x18\x9a\xf4\x03 \x01(\x08:5\n\nprotosizer\x12\x1f.google.protobuf.MessageOptions\x18\x9c\xf4\x03 \x01(\x08:2\n\x07compare\x12\x1f.google.protobuf.MessageOptions\x18\x9d\xf4\x03 \x01(\x08:3\n\x08typedecl\x12\x1f.google.protobuf.MessageOptions\x18\x9e\xf4\x03 \x01(\x08:6\n\x0bmessagename\x12\x1f.google.protobuf.MessageOptions\x18\xa1\xf4\x03 \x01(\x08:<\n\x11goproto_sizecache\x12\x1f.google.protobuf.MessageOptions\x18\xa2\xf4\x03 \x01(\x08::\n\x0fgoproto_unkeyed\x12\x1f.google.protobuf.MessageOptions\x18\xa3\xf4\x03 \x01(\x08:1\n\x08nullable\x12\x1d.google.protobuf.FieldOptions\x18\xe9\xfb\x03 \x01(\x08:.\n\x05embed\x12\x1d.google.protobuf.FieldOptions\x18\xea\xfb\x03 \x01(\x08:3\n\ncustomtype\x12\x1d.google.protobuf.FieldOptions\x18\xeb\xfb\x03 \x01(\t:3\n\ncustomname\x12\x1d.google.protobuf.FieldOptions\x18\xec\xfb\x03 \x01(\t:0\n\x07jsontag\x12\x1d.google.protobuf.FieldOptions\x18\xed\xfb\x03 \x01(\t:1\n\x08moretags\x12\x1d.google.protobuf.FieldOptions\x18\xee\xfb\x03 \x01(\t:1\n\x08casttype\x12\x1d.google.protobuf.FieldOptions\x18\xef\xfb\x03 \x01(\t:0\n\x07castkey\x12\x1d.google.protobuf.FieldOptions\x18\xf0\xfb\x03 \x01(\t:2\n\tcastvalue\x12\x1d.google.protobuf.FieldOptions\x18\xf1\xfb\x03 \x01(\t:0\n\x07stdtime\x12\x1d.google.protobuf.FieldOptions\x18\xf2\xfb\x03 \x01(\x08:4\n\x0bstdduration\x12\x1d.google.protobuf.FieldOptions\x18\xf3\xfb\x03 \x01(\x08:3\n\nwktpointer\x12\x1d.google.protobuf.FieldOptions\x18\xf4\xfb\x03 \x01(\x08:5\n\x0ccastrepeated\x12\x1d.google.protobuf.FieldOptions\x18\xf5\xfb\x03 \x01(\tBE\n\x13com.google.protobufB\nGoGoProtosZ"github.com/gogo/protobuf/gogoproto', dependencies=[google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR])
GOPROTO_ENUM_PREFIX_FIELD_NUMBER = 62001
goproto_enum_prefix = _descriptor.FieldDescriptor(name='goproto_enum_prefix', full_name='gogoproto.goproto_enum_prefix', index=0, number=62001, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_ENUM_STRINGER_FIELD_NUMBER = 62021
goproto_enum_stringer = _descriptor.FieldDescriptor(name='goproto_enum_stringer', full_name='gogoproto.goproto_enum_stringer', index=1, number=62021, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ENUM_STRINGER_FIELD_NUMBER = 62022
enum_stringer = _descriptor.FieldDescriptor(name='enum_stringer', full_name='gogoproto.enum_stringer', index=2, number=62022, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ENUM_CUSTOMNAME_FIELD_NUMBER = 62023
enum_customname = _descriptor.FieldDescriptor(name='enum_customname', full_name='gogoproto.enum_customname', index=3, number=62023, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ENUMDECL_FIELD_NUMBER = 62024
enumdecl = _descriptor.FieldDescriptor(name='enumdecl', full_name='gogoproto.enumdecl', index=4, number=62024, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ENUMVALUE_CUSTOMNAME_FIELD_NUMBER = 66001
enumvalue_customname = _descriptor.FieldDescriptor(name='enumvalue_customname', full_name='gogoproto.enumvalue_customname', index=5, number=66001, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_GETTERS_ALL_FIELD_NUMBER = 63001
goproto_getters_all = _descriptor.FieldDescriptor(name='goproto_getters_all', full_name='gogoproto.goproto_getters_all', index=6, number=63001, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_ENUM_PREFIX_ALL_FIELD_NUMBER = 63002
goproto_enum_prefix_all = _descriptor.FieldDescriptor(name='goproto_enum_prefix_all', full_name='gogoproto.goproto_enum_prefix_all', index=7, number=63002, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_STRINGER_ALL_FIELD_NUMBER = 63003
goproto_stringer_all = _descriptor.FieldDescriptor(name='goproto_stringer_all', full_name='gogoproto.goproto_stringer_all', index=8, number=63003, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
VERBOSE_EQUAL_ALL_FIELD_NUMBER = 63004
verbose_equal_all = _descriptor.FieldDescriptor(name='verbose_equal_all', full_name='gogoproto.verbose_equal_all', index=9, number=63004, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
FACE_ALL_FIELD_NUMBER = 63005
face_all = _descriptor.FieldDescriptor(name='face_all', full_name='gogoproto.face_all', index=10, number=63005, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOSTRING_ALL_FIELD_NUMBER = 63006
gostring_all = _descriptor.FieldDescriptor(name='gostring_all', full_name='gogoproto.gostring_all', index=11, number=63006, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
POPULATE_ALL_FIELD_NUMBER = 63007
populate_all = _descriptor.FieldDescriptor(name='populate_all', full_name='gogoproto.populate_all', index=12, number=63007, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
STRINGER_ALL_FIELD_NUMBER = 63008
stringer_all = _descriptor.FieldDescriptor(name='stringer_all', full_name='gogoproto.stringer_all', index=13, number=63008, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ONLYONE_ALL_FIELD_NUMBER = 63009
onlyone_all = _descriptor.FieldDescriptor(name='onlyone_all', full_name='gogoproto.onlyone_all', index=14, number=63009, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
EQUAL_ALL_FIELD_NUMBER = 63013
equal_all = _descriptor.FieldDescriptor(name='equal_all', full_name='gogoproto.equal_all', index=15, number=63013, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
DESCRIPTION_ALL_FIELD_NUMBER = 63014
description_all = _descriptor.FieldDescriptor(name='description_all', full_name='gogoproto.description_all', index=16, number=63014, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
TESTGEN_ALL_FIELD_NUMBER = 63015
testgen_all = _descriptor.FieldDescriptor(name='testgen_all', full_name='gogoproto.testgen_all', index=17, number=63015, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
BENCHGEN_ALL_FIELD_NUMBER = 63016
benchgen_all = _descriptor.FieldDescriptor(name='benchgen_all', full_name='gogoproto.benchgen_all', index=18, number=63016, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
MARSHALER_ALL_FIELD_NUMBER = 63017
marshaler_all = _descriptor.FieldDescriptor(name='marshaler_all', full_name='gogoproto.marshaler_all', index=19, number=63017, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
UNMARSHALER_ALL_FIELD_NUMBER = 63018
unmarshaler_all = _descriptor.FieldDescriptor(name='unmarshaler_all', full_name='gogoproto.unmarshaler_all', index=20, number=63018, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
STABLE_MARSHALER_ALL_FIELD_NUMBER = 63019
stable_marshaler_all = _descriptor.FieldDescriptor(name='stable_marshaler_all', full_name='gogoproto.stable_marshaler_all', index=21, number=63019, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
SIZER_ALL_FIELD_NUMBER = 63020
sizer_all = _descriptor.FieldDescriptor(name='sizer_all', full_name='gogoproto.sizer_all', index=22, number=63020, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_ENUM_STRINGER_ALL_FIELD_NUMBER = 63021
goproto_enum_stringer_all = _descriptor.FieldDescriptor(name='goproto_enum_stringer_all', full_name='gogoproto.goproto_enum_stringer_all', index=23, number=63021, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ENUM_STRINGER_ALL_FIELD_NUMBER = 63022
enum_stringer_all = _descriptor.FieldDescriptor(name='enum_stringer_all', full_name='gogoproto.enum_stringer_all', index=24, number=63022, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
UNSAFE_MARSHALER_ALL_FIELD_NUMBER = 63023
unsafe_marshaler_all = _descriptor.FieldDescriptor(name='unsafe_marshaler_all', full_name='gogoproto.unsafe_marshaler_all', index=25, number=63023, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
UNSAFE_UNMARSHALER_ALL_FIELD_NUMBER = 63024
unsafe_unmarshaler_all = _descriptor.FieldDescriptor(name='unsafe_unmarshaler_all', full_name='gogoproto.unsafe_unmarshaler_all', index=26, number=63024, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_EXTENSIONS_MAP_ALL_FIELD_NUMBER = 63025
goproto_extensions_map_all = _descriptor.FieldDescriptor(name='goproto_extensions_map_all', full_name='gogoproto.goproto_extensions_map_all', index=27, number=63025, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_UNRECOGNIZED_ALL_FIELD_NUMBER = 63026
goproto_unrecognized_all = _descriptor.FieldDescriptor(name='goproto_unrecognized_all', full_name='gogoproto.goproto_unrecognized_all', index=28, number=63026, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOGOPROTO_IMPORT_FIELD_NUMBER = 63027
gogoproto_import = _descriptor.FieldDescriptor(name='gogoproto_import', full_name='gogoproto.gogoproto_import', index=29, number=63027, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
PROTOSIZER_ALL_FIELD_NUMBER = 63028
protosizer_all = _descriptor.FieldDescriptor(name='protosizer_all', full_name='gogoproto.protosizer_all', index=30, number=63028, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
COMPARE_ALL_FIELD_NUMBER = 63029
compare_all = _descriptor.FieldDescriptor(name='compare_all', full_name='gogoproto.compare_all', index=31, number=63029, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
TYPEDECL_ALL_FIELD_NUMBER = 63030
typedecl_all = _descriptor.FieldDescriptor(name='typedecl_all', full_name='gogoproto.typedecl_all', index=32, number=63030, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ENUMDECL_ALL_FIELD_NUMBER = 63031
enumdecl_all = _descriptor.FieldDescriptor(name='enumdecl_all', full_name='gogoproto.enumdecl_all', index=33, number=63031, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_REGISTRATION_FIELD_NUMBER = 63032
goproto_registration = _descriptor.FieldDescriptor(name='goproto_registration', full_name='gogoproto.goproto_registration', index=34, number=63032, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
MESSAGENAME_ALL_FIELD_NUMBER = 63033
messagename_all = _descriptor.FieldDescriptor(name='messagename_all', full_name='gogoproto.messagename_all', index=35, number=63033, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_SIZECACHE_ALL_FIELD_NUMBER = 63034
goproto_sizecache_all = _descriptor.FieldDescriptor(name='goproto_sizecache_all', full_name='gogoproto.goproto_sizecache_all', index=36, number=63034, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_UNKEYED_ALL_FIELD_NUMBER = 63035
goproto_unkeyed_all = _descriptor.FieldDescriptor(name='goproto_unkeyed_all', full_name='gogoproto.goproto_unkeyed_all', index=37, number=63035, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_GETTERS_FIELD_NUMBER = 64001
goproto_getters = _descriptor.FieldDescriptor(name='goproto_getters', full_name='gogoproto.goproto_getters', index=38, number=64001, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_STRINGER_FIELD_NUMBER = 64003
goproto_stringer = _descriptor.FieldDescriptor(name='goproto_stringer', full_name='gogoproto.goproto_stringer', index=39, number=64003, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
VERBOSE_EQUAL_FIELD_NUMBER = 64004
verbose_equal = _descriptor.FieldDescriptor(name='verbose_equal', full_name='gogoproto.verbose_equal', index=40, number=64004, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
FACE_FIELD_NUMBER = 64005
face = _descriptor.FieldDescriptor(name='face', full_name='gogoproto.face', index=41, number=64005, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOSTRING_FIELD_NUMBER = 64006
gostring = _descriptor.FieldDescriptor(name='gostring', full_name='gogoproto.gostring', index=42, number=64006, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
POPULATE_FIELD_NUMBER = 64007
populate = _descriptor.FieldDescriptor(name='populate', full_name='gogoproto.populate', index=43, number=64007, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
STRINGER_FIELD_NUMBER = 67008
stringer = _descriptor.FieldDescriptor(name='stringer', full_name='gogoproto.stringer', index=44, number=67008, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
ONLYONE_FIELD_NUMBER = 64009
onlyone = _descriptor.FieldDescriptor(name='onlyone', full_name='gogoproto.onlyone', index=45, number=64009, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
EQUAL_FIELD_NUMBER = 64013
equal = _descriptor.FieldDescriptor(name='equal', full_name='gogoproto.equal', index=46, number=64013, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
DESCRIPTION_FIELD_NUMBER = 64014
description = _descriptor.FieldDescriptor(name='description', full_name='gogoproto.description', index=47, number=64014, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
TESTGEN_FIELD_NUMBER = 64015
testgen = _descriptor.FieldDescriptor(name='testgen', full_name='gogoproto.testgen', index=48, number=64015, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
BENCHGEN_FIELD_NUMBER = 64016
benchgen = _descriptor.FieldDescriptor(name='benchgen', full_name='gogoproto.benchgen', index=49, number=64016, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
MARSHALER_FIELD_NUMBER = 64017
marshaler = _descriptor.FieldDescriptor(name='marshaler', full_name='gogoproto.marshaler', index=50, number=64017, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
UNMARSHALER_FIELD_NUMBER = 64018
unmarshaler = _descriptor.FieldDescriptor(name='unmarshaler', full_name='gogoproto.unmarshaler', index=51, number=64018, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
STABLE_MARSHALER_FIELD_NUMBER = 64019
stable_marshaler = _descriptor.FieldDescriptor(name='stable_marshaler', full_name='gogoproto.stable_marshaler', index=52, number=64019, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
SIZER_FIELD_NUMBER = 64020
sizer = _descriptor.FieldDescriptor(name='sizer', full_name='gogoproto.sizer', index=53, number=64020, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
UNSAFE_MARSHALER_FIELD_NUMBER = 64023
unsafe_marshaler = _descriptor.FieldDescriptor(name='unsafe_marshaler', full_name='gogoproto.unsafe_marshaler', index=54, number=64023, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
UNSAFE_UNMARSHALER_FIELD_NUMBER = 64024
unsafe_unmarshaler = _descriptor.FieldDescriptor(name='unsafe_unmarshaler', full_name='gogoproto.unsafe_unmarshaler', index=55, number=64024, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_EXTENSIONS_MAP_FIELD_NUMBER = 64025
goproto_extensions_map = _descriptor.FieldDescriptor(name='goproto_extensions_map', full_name='gogoproto.goproto_extensions_map', index=56, number=64025, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_UNRECOGNIZED_FIELD_NUMBER = 64026
goproto_unrecognized = _descriptor.FieldDescriptor(name='goproto_unrecognized', full_name='gogoproto.goproto_unrecognized', index=57, number=64026, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
PROTOSIZER_FIELD_NUMBER = 64028
protosizer = _descriptor.FieldDescriptor(name='protosizer', full_name='gogoproto.protosizer', index=58, number=64028, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
COMPARE_FIELD_NUMBER = 64029
compare = _descriptor.FieldDescriptor(name='compare', full_name='gogoproto.compare', index=59, number=64029, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
TYPEDECL_FIELD_NUMBER = 64030
typedecl = _descriptor.FieldDescriptor(name='typedecl', full_name='gogoproto.typedecl', index=60, number=64030, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
MESSAGENAME_FIELD_NUMBER = 64033
messagename = _descriptor.FieldDescriptor(name='messagename', full_name='gogoproto.messagename', index=61, number=64033, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_SIZECACHE_FIELD_NUMBER = 64034
goproto_sizecache = _descriptor.FieldDescriptor(name='goproto_sizecache', full_name='gogoproto.goproto_sizecache', index=62, number=64034, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
GOPROTO_UNKEYED_FIELD_NUMBER = 64035
goproto_unkeyed = _descriptor.FieldDescriptor(name='goproto_unkeyed', full_name='gogoproto.goproto_unkeyed', index=63, number=64035, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
NULLABLE_FIELD_NUMBER = 65001
nullable = _descriptor.FieldDescriptor(name='nullable', full_name='gogoproto.nullable', index=64, number=65001, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
EMBED_FIELD_NUMBER = 65002
embed = _descriptor.FieldDescriptor(name='embed', full_name='gogoproto.embed', index=65, number=65002, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
CUSTOMTYPE_FIELD_NUMBER = 65003
customtype = _descriptor.FieldDescriptor(name='customtype', full_name='gogoproto.customtype', index=66, number=65003, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
CUSTOMNAME_FIELD_NUMBER = 65004
customname = _descriptor.FieldDescriptor(name='customname', full_name='gogoproto.customname', index=67, number=65004, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
JSONTAG_FIELD_NUMBER = 65005
jsontag = _descriptor.FieldDescriptor(name='jsontag', full_name='gogoproto.jsontag', index=68, number=65005, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
MORETAGS_FIELD_NUMBER = 65006
moretags = _descriptor.FieldDescriptor(name='moretags', full_name='gogoproto.moretags', index=69, number=65006, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
CASTTYPE_FIELD_NUMBER = 65007
casttype = _descriptor.FieldDescriptor(name='casttype', full_name='gogoproto.casttype', index=70, number=65007, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
CASTKEY_FIELD_NUMBER = 65008
castkey = _descriptor.FieldDescriptor(name='castkey', full_name='gogoproto.castkey', index=71, number=65008, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
CASTVALUE_FIELD_NUMBER = 65009
castvalue = _descriptor.FieldDescriptor(name='castvalue', full_name='gogoproto.castvalue', index=72, number=65009, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
STDTIME_FIELD_NUMBER = 65010
stdtime = _descriptor.FieldDescriptor(name='stdtime', full_name='gogoproto.stdtime', index=73, number=65010, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
STDDURATION_FIELD_NUMBER = 65011
stdduration = _descriptor.FieldDescriptor(name='stdduration', full_name='gogoproto.stdduration', index=74, number=65011, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
WKTPOINTER_FIELD_NUMBER = 65012
wktpointer = _descriptor.FieldDescriptor(name='wktpointer', full_name='gogoproto.wktpointer', index=75, number=65012, type=8, cpp_type=7, label=1, has_default_value=False, default_value=False, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
CASTREPEATED_FIELD_NUMBER = 65013
castrepeated = _descriptor.FieldDescriptor(name='castrepeated', full_name='gogoproto.castrepeated', index=76, number=65013, type=9, cpp_type=9, label=1, has_default_value=False, default_value=b''.decode('utf-8'), message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
DESCRIPTOR.extensions_by_name['goproto_enum_prefix'] = goproto_enum_prefix
DESCRIPTOR.extensions_by_name['goproto_enum_stringer'] = goproto_enum_stringer
DESCRIPTOR.extensions_by_name['enum_stringer'] = enum_stringer
DESCRIPTOR.extensions_by_name['enum_customname'] = enum_customname
DESCRIPTOR.extensions_by_name['enumdecl'] = enumdecl
DESCRIPTOR.extensions_by_name['enumvalue_customname'] = enumvalue_customname
DESCRIPTOR.extensions_by_name['goproto_getters_all'] = goproto_getters_all
DESCRIPTOR.extensions_by_name['goproto_enum_prefix_all'] = goproto_enum_prefix_all
DESCRIPTOR.extensions_by_name['goproto_stringer_all'] = goproto_stringer_all
DESCRIPTOR.extensions_by_name['verbose_equal_all'] = verbose_equal_all
DESCRIPTOR.extensions_by_name['face_all'] = face_all
DESCRIPTOR.extensions_by_name['gostring_all'] = gostring_all
DESCRIPTOR.extensions_by_name['populate_all'] = populate_all
DESCRIPTOR.extensions_by_name['stringer_all'] = stringer_all
DESCRIPTOR.extensions_by_name['onlyone_all'] = onlyone_all
DESCRIPTOR.extensions_by_name['equal_all'] = equal_all
DESCRIPTOR.extensions_by_name['description_all'] = description_all
DESCRIPTOR.extensions_by_name['testgen_all'] = testgen_all
DESCRIPTOR.extensions_by_name['benchgen_all'] = benchgen_all
DESCRIPTOR.extensions_by_name['marshaler_all'] = marshaler_all
DESCRIPTOR.extensions_by_name['unmarshaler_all'] = unmarshaler_all
DESCRIPTOR.extensions_by_name['stable_marshaler_all'] = stable_marshaler_all
DESCRIPTOR.extensions_by_name['sizer_all'] = sizer_all
DESCRIPTOR.extensions_by_name['goproto_enum_stringer_all'] = goproto_enum_stringer_all
DESCRIPTOR.extensions_by_name['enum_stringer_all'] = enum_stringer_all
DESCRIPTOR.extensions_by_name['unsafe_marshaler_all'] = unsafe_marshaler_all
DESCRIPTOR.extensions_by_name['unsafe_unmarshaler_all'] = unsafe_unmarshaler_all
DESCRIPTOR.extensions_by_name['goproto_extensions_map_all'] = goproto_extensions_map_all
DESCRIPTOR.extensions_by_name['goproto_unrecognized_all'] = goproto_unrecognized_all
DESCRIPTOR.extensions_by_name['gogoproto_import'] = gogoproto_import
DESCRIPTOR.extensions_by_name['protosizer_all'] = protosizer_all
DESCRIPTOR.extensions_by_name['compare_all'] = compare_all
DESCRIPTOR.extensions_by_name['typedecl_all'] = typedecl_all
DESCRIPTOR.extensions_by_name['enumdecl_all'] = enumdecl_all
DESCRIPTOR.extensions_by_name['goproto_registration'] = goproto_registration
DESCRIPTOR.extensions_by_name['messagename_all'] = messagename_all
DESCRIPTOR.extensions_by_name['goproto_sizecache_all'] = goproto_sizecache_all
DESCRIPTOR.extensions_by_name['goproto_unkeyed_all'] = goproto_unkeyed_all
DESCRIPTOR.extensions_by_name['goproto_getters'] = goproto_getters
DESCRIPTOR.extensions_by_name['goproto_stringer'] = goproto_stringer
DESCRIPTOR.extensions_by_name['verbose_equal'] = verbose_equal
DESCRIPTOR.extensions_by_name['face'] = face
DESCRIPTOR.extensions_by_name['gostring'] = gostring
DESCRIPTOR.extensions_by_name['populate'] = populate
DESCRIPTOR.extensions_by_name['stringer'] = stringer
DESCRIPTOR.extensions_by_name['onlyone'] = onlyone
DESCRIPTOR.extensions_by_name['equal'] = equal
DESCRIPTOR.extensions_by_name['description'] = description
DESCRIPTOR.extensions_by_name['testgen'] = testgen
DESCRIPTOR.extensions_by_name['benchgen'] = benchgen
DESCRIPTOR.extensions_by_name['marshaler'] = marshaler
DESCRIPTOR.extensions_by_name['unmarshaler'] = unmarshaler
DESCRIPTOR.extensions_by_name['stable_marshaler'] = stable_marshaler
DESCRIPTOR.extensions_by_name['sizer'] = sizer
DESCRIPTOR.extensions_by_name['unsafe_marshaler'] = unsafe_marshaler
DESCRIPTOR.extensions_by_name['unsafe_unmarshaler'] = unsafe_unmarshaler
DESCRIPTOR.extensions_by_name['goproto_extensions_map'] = goproto_extensions_map
DESCRIPTOR.extensions_by_name['goproto_unrecognized'] = goproto_unrecognized
DESCRIPTOR.extensions_by_name['protosizer'] = protosizer
DESCRIPTOR.extensions_by_name['compare'] = compare
DESCRIPTOR.extensions_by_name['typedecl'] = typedecl
DESCRIPTOR.extensions_by_name['messagename'] = messagename
DESCRIPTOR.extensions_by_name['goproto_sizecache'] = goproto_sizecache
DESCRIPTOR.extensions_by_name['goproto_unkeyed'] = goproto_unkeyed
DESCRIPTOR.extensions_by_name['nullable'] = nullable
DESCRIPTOR.extensions_by_name['embed'] = embed
DESCRIPTOR.extensions_by_name['customtype'] = customtype
DESCRIPTOR.extensions_by_name['customname'] = customname
DESCRIPTOR.extensions_by_name['jsontag'] = jsontag
DESCRIPTOR.extensions_by_name['moretags'] = moretags
DESCRIPTOR.extensions_by_name['casttype'] = casttype
DESCRIPTOR.extensions_by_name['castkey'] = castkey
DESCRIPTOR.extensions_by_name['castvalue'] = castvalue
DESCRIPTOR.extensions_by_name['stdtime'] = stdtime
DESCRIPTOR.extensions_by_name['stdduration'] = stdduration
DESCRIPTOR.extensions_by_name['wktpointer'] = wktpointer
DESCRIPTOR.extensions_by_name['castrepeated'] = castrepeated
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(goproto_enum_prefix)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(goproto_enum_stringer)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_stringer)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enum_customname)
google_dot_protobuf_dot_descriptor__pb2.EnumOptions.RegisterExtension(enumdecl)
google_dot_protobuf_dot_descriptor__pb2.EnumValueOptions.RegisterExtension(enumvalue_customname)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_getters_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_enum_prefix_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_stringer_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(verbose_equal_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(face_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(gostring_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(populate_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(stringer_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(onlyone_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(equal_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(description_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(testgen_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(benchgen_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(marshaler_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unmarshaler_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(stable_marshaler_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(sizer_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_enum_stringer_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(enum_stringer_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unsafe_marshaler_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(unsafe_unmarshaler_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_extensions_map_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_unrecognized_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(gogoproto_import)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(protosizer_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(compare_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(typedecl_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(enumdecl_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_registration)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(messagename_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_sizecache_all)
google_dot_protobuf_dot_descriptor__pb2.FileOptions.RegisterExtension(goproto_unkeyed_all)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_getters)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_stringer)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(verbose_equal)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(face)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(gostring)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(populate)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(stringer)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(onlyone)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(equal)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(description)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(testgen)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(benchgen)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(marshaler)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unmarshaler)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(stable_marshaler)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(sizer)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unsafe_marshaler)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(unsafe_unmarshaler)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_extensions_map)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_unrecognized)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(protosizer)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(compare)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(typedecl)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(messagename)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_sizecache)
google_dot_protobuf_dot_descriptor__pb2.MessageOptions.RegisterExtension(goproto_unkeyed)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(nullable)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(embed)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(customtype)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(customname)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(jsontag)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(moretags)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(casttype)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castkey)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castvalue)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stdtime)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(stdduration)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(wktpointer)
google_dot_protobuf_dot_descriptor__pb2.FieldOptions.RegisterExtension(castrepeated)
DESCRIPTOR._options = None
