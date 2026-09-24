from Crypto.Cipher import DES, DES3
from Crypto.Hash import MD5, SHA1
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import hashlib


# Legacy symmetric encryption
DES_KEY = b"8bytekey"

def encrypt_des(data: bytes) -> bytes:
    cipher = DES.new(DES_KEY, DES.MODE_ECB)
    padded = data + b"\x00" * ((8 - len(data) % 8) % 8)
    return cipher.encrypt(padded)


# Legacy 3DES
TRIPLE_DES_KEY = b"123456789012345678901234"

def encrypt_3des(data: bytes) -> bytes:
    cipher = DES3.new(TRIPLE_DES_KEY, DES3.MODE_ECB)
    padded = data + b"\x00" * ((8 - len(data) % 8) % 8)
    return cipher.encrypt(padded)


# Weak hashes
def md5_hash(data: str) -> str:
    return hashlib.md5(data.encode()).hexdigest()


def sha1_hash(data: str) -> str:
    return hashlib.sha1(data.encode()).hexdigest()


# Weak RSA key
RSA_KEY = RSA.generate(1024)

def rsa_encrypt(data: bytes) -> bytes:
    cipher = PKCS1_v1_5.new(RSA_KEY.publickey())
    return cipher.encrypt(data)