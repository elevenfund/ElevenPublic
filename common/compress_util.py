import gzip
from io import BytesIO

def compress_text(text: str) -> bytes:
    buf = BytesIO()
    with gzip.GzipFile(fileobj=buf, mode='wb') as f:
        f.write(text.encode('utf-8'))
    return buf.getvalue()

def decompress_text(data: bytes) -> str:
    buf = BytesIO(data)
    with gzip.GzipFile(fileobj=buf, mode='rb') as f:
        return f.read().decode('utf-8') 