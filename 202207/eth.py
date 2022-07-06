from eth_account import Account
from eth_account.messages import encode_defunct
from eth_keys import keys
from hexbytes import HexBytes

acct = Account.create('KEYSMASH FJAFJKLDSKF7JKFDJ 1530')
print(acct.__dict__)
print(acct.key, type(acct.key))
print(acct.address)

priv_key = keys.PrivateKey(acct.key)
print(priv_key)
pub_key = priv_key.public_key

# test_hex(hex_sha256)
hb = HexBytes('2b3e728c1a5d1efa035c307c22f80e47f870db5795e2f7a8cef599df5193a796')
priv_key = keys.PrivateKey(hb)
print(priv_key)
print(priv_key.public_key)
print(priv_key.__dict__)
"0xE7F8d8798fd79C94916eEb24F44c67195922544a"
acc = Account.privateKeyToAccount(priv_key)
print(acc.address)

print()
msg = encode_defunct(text="ok")
print(msg)
sign_message = acc.sign_message(msg)
print(sign_message)

print(sign_message.messageHash)



# crypto
