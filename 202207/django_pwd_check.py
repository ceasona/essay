import base64
import datetime
import hashlib
from decimal import Decimal

_PROTECTED_TYPES = (
    type(None), int, float, Decimal, datetime.datetime, datetime.date, datetime.time,
)


def force_bytes(s, encoding='utf-8', strings_only=False, errors='strict'):
    """
    Similar to smart_bytes, except that lazy instances are resolved to
    strings, rather than kept as lazy objects.

    If strings_only is True, don't convert (some) non-string-like objects.
    """
    # Handle the common case first for performance reasons.
    if isinstance(s, bytes):
        if encoding == 'utf-8':
            return s
        else:
            return s.decode('utf-8', errors).encode(encoding, errors)
    if strings_only and isinstance(s, _PROTECTED_TYPES):
        return s
    if isinstance(s, memoryview):
        return bytes(s)
    return str(s).encode(encoding, errors)


def pbkdf2(password, salt, iterations, dklen=0, digest=None):
    """Return the hash of password using pbkdf2."""
    if digest is None:
        digest = hashlib.sha256
    dklen = dklen or None
    password = force_bytes(password)
    salt = force_bytes(salt)
    return hashlib.pbkdf2_hmac(digest().name, password, salt, iterations, dklen)


def encode(password, salt, iterations=None):
    assert password is not None
    assert salt and '$' not in salt
    hash = pbkdf2(password, salt, iterations, digest=hashlib.sha256)
    hash = base64.b64encode(hash).decode('ascii').strip()
    return "%s$%d$%s$%s" % ("pbkdf2_sha256", iterations, salt, hash)


db_pwd = "pbkdf2_sha256$260000$o7g1mO3rLbSEKbF9VCVNoP$pCFDqwk6kXmhU0OCsXbVGmC2ZvpCSbWlZjA1OOIdvuM="
# db_pwd = "pbkdf2-sha256$260000$NAYAAKDUGuMcQ6hVqtX6Pw$nKhMkfefzrQ1ScHqq68Zt6FXGMfdT1eJTB1g3VAOaT4"
password = "shucangdao123"
# salt = "o7g1mO3rLbSEKbF9VCVNoP"
# iterations = 260000
algorithm, iterations, salt, hash = db_pwd.split('$', 3)
print(password, salt, iterations)
print(encode(password, salt, int(iterations)))



