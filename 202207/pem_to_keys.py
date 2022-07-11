import base64
import codecs
import os
from pathlib import Path
from ecdsa import SigningKey



def get_private_key(pem_file):
    return SigningKey.from_pem(pem_file.read())


secp256k1_key = open(os.path.join(Path(__file__).parent, "secp256k1-key.pem"), 'r', encoding='utf8')
ecpubkey = open(os.path.join(Path(__file__).parent, "ecpubkey.pem"), 'r', encoding='utf8')

# print(get_private_key(secp256k1_key).to_string())
pk = get_private_key(secp256k1_key)
pk_bytes = pk.to_string()

print('0x' + codecs.decode(codecs.encode(pk_bytes, 'hex'), 'ascii'))

pub_k_bytes = pk.get_verifying_key().to_string()
pub_k_hex_str = '0x' + codecs.decode(codecs.encode(pub_k_bytes, 'hex'), 'ascii')
print(pub_k_hex_str)
print(len(pub_k_hex_str))


def unpem(pem):
    d = ("").join(
        [
            l.strip()
            for l in pem.split(("\n"))
            if l and not l.startswith(("-----"))
        ]
    )
    return base64.b64decode(d)

print('\n', "[unpem]")
pub_unpem = unpem(ecpubkey.read())
pub_k_hex_str_from_pem = '0x' + codecs.decode(codecs.encode(pub_unpem, 'hex'), 'ascii')
print("公钥all：", pub_k_hex_str_from_pem)
print(len(pub_k_hex_str_from_pem))

pk_unpem = unpem(open(os.path.join(Path(__file__).parent, "secp256k1-key.pem"), 'r', encoding='utf8').read())
pk_hex_str_from_pem = '0x' + codecs.decode(codecs.encode(pk_unpem, 'hex'), 'ascii')
print("私钥all：", pk_hex_str_from_pem)
