import hashlib
import os


def store_password(password: str):
    salt = os.urandom(16)

    password_hash = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return salt.hex(), password_hash.hex()


def verify_password(password: str, salt_hex: str, stored_hash: str) -> bool:
    salt = bytes.fromhex(salt_hex)

    password_hash = hashlib.scrypt(
        password.encode(),
        salt=salt,
        n=2**14,
        r=8,
        p=1
    )

    return password_hash.hex() == stored_hash