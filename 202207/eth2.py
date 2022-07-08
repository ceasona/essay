from eth_account import Account
from hexbytes import HexBytes
from web3.auto import w3
from eth_keys import keys
from eth_account.messages import encode_defunct

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

# Verify a Message
# message = encode_defunct(text="I♥SF")
msg_from = w3.eth.account.recover_message(message, signature=signed_message.signature)
print('[msg_from1]:', msg_from)

# Verify a Message from message hash
msg_from = w3.eth.account.recoverHash(signed_message.messageHash, signature=signed_message.signature)
print('[msg_from2]:', msg_from)
