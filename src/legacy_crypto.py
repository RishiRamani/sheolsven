from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


AES_KEY = bytes.fromhex(
    "9f86d081884c7d659a2feaa0c55ad015"
    "a3bf4f1b2b0b822cd15d6c15b0f00a08"
)


def encrypt_data(data: bytes) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_GCM)
    ciphertext, tag = cipher.encrypt_and_digest(data)

    return cipher.nonce + tag + ciphertext


def sha256_hash(data: str) -> str:
    return SHA256.new(data.encode()).hexdigest()


# Stronger RSA configuration
RSA_KEY = RSA.generate(3072)


def rsa_encrypt(data: bytes) -> bytes:
    cipher = PKCS1_OAEP.new(RSA_KEY.publickey())
    return cipher.encrypt(data)