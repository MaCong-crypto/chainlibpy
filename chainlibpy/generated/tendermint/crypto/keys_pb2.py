
'Generated protocol buffer code.'
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
_sym_db = _symbol_database.Default()
from ...gogoproto import gogo_pb2 as gogoproto_dot_gogo__pb2
DESCRIPTOR = _descriptor.FileDescriptor(name='tendermint/crypto/keys.proto', package='tendermint.crypto', syntax='proto3', serialized_options=b'Z8github.com/tendermint/tendermint/proto/tendermint/crypto', create_key=_descriptor._internal_create_key, serialized_pb=b'\n\x1ctendermint/crypto/keys.proto\x12\x11tendermint.crypto\x1a\x14gogoproto/gogo.proto"D\n\tPublicKey\x12\x11\n\x07ed25519\x18\x01 \x01(\x0cH\x00\x12\x13\n\tsecp256k1\x18\x02 \x01(\x0cH\x00:\x08\xe8\xa1\x1f\x01\xe8\xa0\x1f\x01B\x05\n\x03sumB:Z8github.com/tendermint/tendermint/proto/tendermint/cryptob\x06proto3', dependencies=[gogoproto_dot_gogo__pb2.DESCRIPTOR])
_PUBLICKEY = _descriptor.Descriptor(name='PublicKey', full_name='tendermint.crypto.PublicKey', filename=None, file=DESCRIPTOR, containing_type=None, create_key=_descriptor._internal_create_key, fields=[_descriptor.FieldDescriptor(name='ed25519', full_name='tendermint.crypto.PublicKey.ed25519', index=0, number=1, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b'', message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key), _descriptor.FieldDescriptor(name='secp256k1', full_name='tendermint.crypto.PublicKey.secp256k1', index=1, number=2, type=12, cpp_type=9, label=1, has_default_value=False, default_value=b'', message_type=None, enum_type=None, containing_type=None, is_extension=False, extension_scope=None, serialized_options=None, file=DESCRIPTOR, create_key=_descriptor._internal_create_key)], extensions=[], nested_types=[], enum_types=[], serialized_options=b'\xe8\xa1\x1f\x01\xe8\xa0\x1f\x01', is_extendable=False, syntax='proto3', extension_ranges=[], oneofs=[_descriptor.OneofDescriptor(name='sum', full_name='tendermint.crypto.PublicKey.sum', index=0, containing_type=None, create_key=_descriptor._internal_create_key, fields=[])], serialized_start=73, serialized_end=141)
_PUBLICKEY.oneofs_by_name['sum'].fields.append(_PUBLICKEY.fields_by_name['ed25519'])
_PUBLICKEY.fields_by_name['ed25519'].containing_oneof = _PUBLICKEY.oneofs_by_name['sum']
_PUBLICKEY.oneofs_by_name['sum'].fields.append(_PUBLICKEY.fields_by_name['secp256k1'])
_PUBLICKEY.fields_by_name['secp256k1'].containing_oneof = _PUBLICKEY.oneofs_by_name['sum']
DESCRIPTOR.message_types_by_name['PublicKey'] = _PUBLICKEY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)
PublicKey = _reflection.GeneratedProtocolMessageType('PublicKey', (_message.Message,), {'DESCRIPTOR': _PUBLICKEY, '__module__': 'tendermint.crypto.keys_pb2'})
_sym_db.RegisterMessage(PublicKey)
DESCRIPTOR._options = None
_PUBLICKEY._options = None
