import base64
import binascii
from gmssl import sm2, func

# 0xA326F697AfDA7bEC7fCfF0C5D579201c98F45546
# 16进制的公钥和私钥
private_key = '00B9AB0B828FF68872F21A837FC303668428DEA11DCD1B24429D0C99E24EED83D5'
print(len(private_key))
# private_key = 'f1ff8c73c3dbd5a66041ea3938acab89b8f8d24df0dae4647eec3dfacd6a7c76'
print(len(private_key))
public_key = 'B9C9A6E04E9C91F7BA880429273747D7EF5DDEB0BB2FF6317EB00BEF331A83081A6994B8993F3F5D6EADDDB81872266C87C018FB4162F5AF347B483E24620207'
print(len(public_key))
sm2_crypt = sm2.CryptSM2(
    public_key=public_key, private_key=private_key)

data = b"111"
enc_data = sm2_crypt.encrypt(data)
dec_data = sm2_crypt.decrypt(enc_data)

assert dec_data == data

