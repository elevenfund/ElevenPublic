from compress_util import compress_text, decompress_text
from crypto_util import encrypt, decrypt


def test_compress_decompress():
    text = 'hello, 世界!'
    compressed = compress_text(text)
    decompressed = decompress_text(compressed)
    assert decompressed == text

def test_encrypt_decrypt():
    data = 'hello, 加密!'.encode('utf-8')
    password = 'testpass123'
    encrypted = encrypt(data, password)
    decrypted = decrypt(encrypted, password)
    assert decrypted == data

if __name__ == '__main__':
    test_compress_decompress()
    test_encrypt_decrypt()
    print('测试通过') 