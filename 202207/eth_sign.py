import codecs
from eth_account import Account
from eth_account._utils.signing import sign_message_hash, to_eth_v, to_bytes32
from eth_keys.backends.native.ecdsa import deterministic_generate_k
from eth_keys.backends.native.jacobian import fast_multiply, inv
from eth_keys.datatypes import Signature
from eth_typing import Hash32
from eth_utils import keccak, big_endian_to_int, to_bytes
from hexbytes import HexBytes
from web3.auto import w3
from eth_keys import keys
from eth_keys.constants import SECPK1_N as N, SECPK1_G as G
from eth_account.messages import encode_defunct, _hash_eip191_message

# Sign a Message
msg = "I♥SF"
hb = HexBytes('1' * 64)
private_key = keys.PrivateKey(hb)
print('[private_key]:', private_key)
print('[address]:', Account.privateKeyToAccount(private_key).address)
message = encode_defunct(text=msg)
print(encode_defunct(hexstr=str(private_key)))
print("[message]:", message)
print("[message]-decode:", message.body.decode('utf8'))
signed_message = w3.eth.account.sign_message(message, private_key=private_key)
print('[signed_message]:', signed_message)

joined = b'\x19' + message.version + message.header + message.body

message_hash = _hash_eip191_message(message)
print(joined)
print('[message_hash_1]:', Hash32(keccak(joined)))
print('[message_hash_2]:', message_hash)
print('[message_hash_hex]:', codecs.decode(codecs.encode(HexBytes(message_hash), 'hex'), 'ascii'))
msg_hash_bytes = HexBytes(message_hash)
print(msg_hash_bytes)

# key = self._parsePrivateKey(private_key)
(v, r, s, eth_signature_bytes) = sign_message_hash(private_key, msg_hash_bytes)

print((v, r, s, eth_signature_bytes))

# eth_keys.backends.native.main.NativeECCBackend -> ecdsa_sign
from eth_keys.backends.native.main import NativeECCBackend


def ecdsa_raw_sign(msg_hash: bytes,
                   private_key_bytes: bytes):
    z = big_endian_to_int(msg_hash)
    k = deterministic_generate_k(msg_hash, private_key_bytes)

    r, y = fast_multiply(G, k)
    s_raw = inv(k, N) * (z + r * big_endian_to_int(private_key_bytes)) % N

    v = 27 + ((y % 2) ^ (0 if s_raw * 2 < N else 1))
    s = s_raw if s_raw * 2 < N else N - s_raw

    return v - 27, r, s


def ecdsa_sign(msg_hash, pri_key):
    signature_vrs = ecdsa_raw_sign(msg_hash, pri_key.to_bytes())
    signature = Signature(vrs=signature_vrs, backend=NativeECCBackend)
    return signature


def my_sign_message_hash(msg_hash, pri_key):
    signature = ecdsa_sign(msg_hash, pri_key)
    (v_raw, r, s) = signature.vrs
    v = to_eth_v(v_raw)
    eth_signature_bytes = to_bytes32(r) + to_bytes32(s) + to_bytes(v)
    return (v, r, s, eth_signature_bytes)


print(my_sign_message_hash(message_hash, private_key))
# SignedMessage(
#             messageHash=msg_hash_bytes,
#             r=r,
#             s=s,
#             v=v,
#             signature=HexBytes(eth_signature_bytes),
#         )

# Verify a Message
# message = encode_defunct(text="I♥SF")
msg_from = w3.eth.account.recover_message(message, signature=signed_message.signature)
print('[msg_from1]:', msg_from)

# Verify a Message from message hash
msg_from = w3.eth.account.recoverHash(signed_message.messageHash, signature=signed_message.signature)
print('[msg_from2]:', msg_from)
