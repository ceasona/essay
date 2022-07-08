import codecs

from eth_account import Account
from eth_keys.backends import NativeECCBackend
from eth_keys.backends.native.ecdsa import encode_raw_public_key
from eth_keys.backends.native.jacobian import fast_multiply
from eth_keys.constants import SECPK1_N, SECPK1_G
from eth_keys.datatypes import PublicKey
from eth_typing import HexStr
from eth_utils import big_endian_to_int, keccak, to_checksum_address, to_normalized_address, remove_0x_prefix, \
    encode_hex, int_to_big_endian
from hexbytes import HexBytes
from eth_keys import keys
from passlib.handlers.digests import hex_sha256

# 0x19E7E376E7C213B7E7e7e46cc70A5dD086DAff2A
# 0x1111111111111111111111111111111111111111111111111111111111111111
# 一个字节8bit
# 16进制 （2 ** 4）** 64

hb = HexBytes('e' * 64)
priv_key = keys.PrivateKey(hb)
print(priv_key)
print('[address]:', Account.from_key(priv_key).address)
key = Account._parsePrivateKey(priv_key)
print(key)
print(type(key))
# 一个字节8bit , 可存放两个16进制数 [（2 ** 8）]** 32
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
    left, right = raw_public_key
    print(len(HexBytes(raw_public_key[0])))
    print(len(HexBytes(raw_public_key[1])))
    # 将int转换为2字节的BigEndian
    # int_to_big_endian(left)
    return public_key_bytes


my_public_key_bytes = private_key_to_public_key(priv_key_byte)

print(my_public_key_bytes)

public_key = PublicKey(my_public_key_bytes, backend=NativeECCBackend())
print('[public_key]:', public_key)

print('\n', "*" * 12, "public_key_to_account", "*" * 12)

# 一个字节存放了两个16进制数，取后20也就相当于后40
address_raw = keccak(my_public_key_bytes)[-20:]
print('[address raw]:', address_raw)
address_ascii = '0x' + codecs.decode(codecs.encode(HexBytes(address_raw), 'hex'), 'ascii')
print('[address ascii]:', address_ascii)

print('[address checksum]:', to_checksum_address(address_raw))

print('\n', "*" * 12, "address checksum", "*" * 12)

custom_address = "0x" + '1' * 34 + 'CEACEA'

norm_address = to_normalized_address(custom_address)
print('[address norm_address]:', norm_address)
remove_0x_prefix = remove_0x_prefix(HexStr(norm_address))
address_hash = keccak(text=remove_0x_prefix)
print('[address hash]:', address_hash)
print('0x' + codecs.decode(codecs.encode(address_hash, 'hex'), 'ascii'))
print(encode_hex(address_hash))

print('--'.join(custom_address[2:]))
print('--'.join(encode_hex(address_hash)[2:42]))
print('[address checksum]:', to_checksum_address(custom_address))
