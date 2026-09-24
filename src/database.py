from Crypto.Cipher import AES
import os


AES_KEY = os.urandom(32)


def encrypt_record(record: bytes) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_GCM)

    ciphertext, tag = cipher.encrypt_and_digest(record)

    return cipher.nonce + tag + ciphertext