from eth_keys.backends import NativeECCBackend
from eth_keys.datatypes import PublicKey
from eth_keys.utils.padding import pad32
from hexbytes import HexBytes

pub_key = "0x3d2e38053f6739ff09c36a5288ef7d8429a48f647dab79fc5052746ad85b40c042ee76ef495519b3a86d224a7326b27fb9d35e887d4cb4fcc895645fd1ec4e80"
print(len(pub_key))
pub_key_l = pub_key[2:66]
pub_key_r = pub_key[66:]
print(len(pub_key_l), pub_key_l)
print(len(pub_key_r), pub_key_r)

pub_key_l_byte = HexBytes(pub_key_l)
pub_key_r_byte = HexBytes(pub_key_r)
print(pub_key_l_byte, len(pub_key_l_byte))


public_key_bytes = b''.join((
        pad32(pub_key_l_byte),
        pad32(pub_key_r_byte),
    ))

print(public_key_bytes, len(public_key_bytes))

public_key = PublicKey(public_key_bytes, backend=NativeECCBackend())
print('[public_key]:', public_key)
print(public_key.to_address())
