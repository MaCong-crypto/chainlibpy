
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...google.api import http_pb2 as google_dot_api_dot_http__pb2
from google.protobuf import descriptor_pb2 as google_dot_protobuf_dot_descriptor__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='google/api/annotations.proto', package='google.api', syntax='proto3', serialized_options=b'\n\x0ecom.google.apiB\x10AnnotationsProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPI', create_key=_descriptor._internal_create_key, serialized_pb=b'\n\x1cgoogle/api/annotations.proto\x12\ngoogle.api\x1a\x15google/api/http.proto\x1a google/protobuf/descriptor.proto:E\n\x04http\x12\x1e.google.protobuf.MethodOptions\x18\xb0\xca\xbc" \x01(\x0b2\x14.google.api.HttpRuleBn\n\x0ecom.google.apiB\x10AnnotationsProtoP\x01ZAgoogle.golang.org/genproto/googleapis/api/annotations;annotations\xa2\x02\x04GAPIb\x06proto3', dependencies=[google_dot_api_dot_http__pb2.DESCRIPTOR, google_dot_protobuf_dot_descriptor__pb2.DESCRIPTOR])
HTTP_FIELD_NUMBER = 72295728
http = _descriptor.FieldDescriptor(name='http', full_name='google.api.http', index=0, number=72295728, type=11, cpp_type=10, label=1, has_default_value=False, default_value=None, message_type=None, enum_type=None, containing_type=None, is_extension=True, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)
DESCRIPTOR.extensions_by_name['http'] = http
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
http.message_type = google_dot_api_dot_http__pb2._HTTPRULE
google_dot_protobuf_dot_descriptor__pb2.MethodOptions.RegisterExtension(http)
DESCRIPTOR._options = None
