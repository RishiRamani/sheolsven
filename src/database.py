from Crypto.Cipher import AES

# Static / hardcoded encryption material
AES_KEY = b"0123456789abcdef"
AES_IV = b"abcdef9876543210"


def encrypt_record(record: bytes) -> bytes:
    cipher = AES.new(AES_KEY, AES.MODE_CBC, AES_IV)

    padded = record + b"\x00" * ((16 - len(record) % 16) % 16)

    return cipher.encrypt(padded)