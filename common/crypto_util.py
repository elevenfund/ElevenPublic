from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib
import base64

def _get_aes_key(password: str) -> bytes:
    return hashlib.sha256(password.encode('utf-8')).digest()

def encrypt(data: bytes, password: str) -> bytes:
    key = _get_aes_key(password)
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CFB, iv)
    encrypted = cipher.encrypt(data)
    return iv + encrypted

def decrypt(enc_data: bytes, password: str) -> bytes:
    key = _get_aes_key(password)
    iv = enc_data[:16]
    cipher = AES.new(key, AES.MODE_CFB, iv)
    return cipher.decrypt(enc_data[16:]) 