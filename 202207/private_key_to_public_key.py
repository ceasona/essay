import codecs

from eth_account import Account
from eth_keys.backends import NativeECCBackend
from eth_keys.backends.native.ecdsa import encode_raw_public_key
from eth_keys.backends.native.jacobian import fast_multiply
from eth_keys.constants import SECPK1_N, SECPK1_G
from eth_keys.datatypes import PublicKey
from eth_utils import big_endian_to_int, keccak, to_checksum_address
from hexbytes import HexBytes
from eth_keys import keys
from passlib.handlers.digests import hex_sha256

# 0x19E7E376E7C213B7E7e7e46cc70A5dD086DAff2A
# 0x1111111111111111111111111111111111111111111111111111111111111111
hb = HexBytes('1' * 64)
priv_key = keys.PrivateKey(hb)
print(priv_key)
print('[address]:', Account.from_key(priv_key).address)
key = Account._parsePrivateKey(priv_key)
print(key)
print(type(key))
# exit(22)
priv_key_byte = priv_key.to_bytes()
print(priv_key_byte)


def private_key_to_public_key(private_key_bytes: bytes) -> bytes:
    # 将16进制数转为10进制大整数
    private_key_as_num = big_endian_to_int(private_key_bytes)
    print(private_key_as_num)
    print(type(private_key_as_num))

    # 限制private key 大小
    if private_key_as_num >= SECPK1_N:
        raise Exception("Invalid privkey")

    # public key 坐标
    # 椭圆曲线G点坐标SECPK1_G
    raw_public_key = fast_multiply(SECPK1_G, private_key_as_num)
    print(raw_public_key)
    # left
    print('0x' + codecs.decode(codecs.encode(HexBytes(raw_public_key[0]), 'hex'), 'ascii'))
    # right
    print('0x' + codecs.decode(codecs.encode(HexBytes(raw_public_key[1]), 'hex'), 'ascii'))
    public_key_bytes = encode_raw_public_key(raw_public_key)
    return public_key_bytes


my_public_key_bytes = private_key_to_public_key(priv_key_byte)

print(my_public_key_bytes)

public_key = PublicKey(my_public_key_bytes, backend=NativeECCBackend())
print('[public_key]:', public_key)

print('\n', "*" * 12, "public_key_to_account", "*" * 12)

address_raw = keccak(my_public_key_bytes)[-20:]

print('[address raw]:', address_raw)
address_ascii = '0x' + codecs.decode(codecs.encode(HexBytes(address_raw), 'hex'), 'ascii')
print('[address ascii]:', address_ascii)

print('[address checksum]:', to_checksum_address(address_raw))
