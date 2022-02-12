import base64
import hashlib

from constants import PWD_HASH_ITERATIONS, PWD_HASH_SALT


def make_user_password_hash(password):

    return base64.b64encode(hashlib.pbkdf2_hmac(
        'sha256',
        password.encode('utf-8'),
        PWD_HASH_SALT,
        PWD_HASH_ITERATIONS
    ))
