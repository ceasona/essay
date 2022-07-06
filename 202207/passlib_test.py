import hashlib

from passlib.hash import pbkdf2_sha256, pbkdf2_sha1, pbkdf2_sha512
from passlib.hash import sha256_crypt, md5_crypt, sha1_crypt, sha512_crypt
from passlib.hash import mssql2000, hex_sha1, hex_md4, hex_md5, hex_sha256, hex_sha512


def test_sha256():
    print(pbkdf2_sha256.default_rounds)
    # generate new salt, and hash a password
    res = pbkdf2_sha256.hash("toomanysecrets", salt=b'1010')
    print(res)
    # '$pbkdf2-sha256$29000$N2YMIWQsBWBMae09x1jrPQ$1t8iyB2A.WF/Z5JZv.lfCIhXXN33N23OSgQYThBYRfk'
    # $pbkdf2-sha256$29000$7j1nLCVECIHQeq81hpCydg$uPOO.JJYDEFYHNCVqmevqZdbj6ercF4dBaEAPJ/M2rc
    # verifying the password
    print(pbkdf2_sha256.verify("toomanysecrets", res))
    print(pbkdf2_sha256.verify("joshua", res))
    custom_pbkdf2 = pbkdf2_sha256.using(rounds=260000)
    print(custom_pbkdf2.default_rounds)
    print(custom_pbkdf2.hash("shucangdao123"))


def test_pbkdf2(handlers):
    print("*" * 6, f"{handlers.__name__}", "*" * 6)
    print("default_rounds:", handlers.default_rounds)
    res = handlers.hash("toomanysecrets", salt=b'1010')
    print(f"response_{handlers.__name__}:", res)
    print()

def test_crypt(handlers):
    print("*" * 6, f"{handlers.__name__}", "*" * 6)
    if "default_rounds" in handlers.__dict__:
        print("default_rounds:", handlers.default_rounds)
    res = handlers.hash("toomanysecrets", salt='wd')
    print(f"response_{handlers.__name__}:", res)
    print(len(res.split("$")[-1]))
    print()

def test_hex(handlers):
    print("*" * 6, f"{handlers.__name__}", "*" * 6)
    if "default_rounds" in handlers.__dict__:
        print("default_rounds:", handlers.default_rounds)
    res = handlers.hash("toomanysecrets")
    print(f"response_{handlers.__name__}:", res)
    print(len(res.split("$")[-1]))
    print()


# test_pbkdf2(pbkdf2_sha1)
# test_pbkdf2(pbkdf2_sha256)
# test_pbkdf2(pbkdf2_sha512)
#
# test_crypt(md5_crypt)
# test_crypt(sha1_crypt)
# test_crypt(sha256_crypt)
# test_crypt(sha512_crypt)

test_hex(hex_md4)
test_hex(hex_md5)
test_hex(hex_sha1)
test_hex(hex_sha256)
test_hex(hex_sha512)


md = hashlib.md5()
md.update('toomanysecrets'.encode('utf-8'))
print(md.hexdigest(), len(md.hexdigest()))
