import os
import sys
import pyperclip
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.compress_util import compress_text
from common.crypto_util import encrypt

GIT_FILE = 'clipboard.enc'

def main():
    password = os.environ.get('CLIPBOARD_PASS')
    if not password:
        print('请先设置环境变量CLIPBOARD_PASS')
        return
    text = pyperclip.paste()
    if not text:
        print('剪切板为空')
        return
    compressed = compress_text(text)
    encrypted = encrypt(compressed, password)
    with open(GIT_FILE, 'wb') as f:
        f.write(encrypted)
    # git add/commit/push
    os.system(f'git add {GIT_FILE}')
    os.system(f'git commit -m "update clipboard"')
    os.system('git push')
    print('已加密并上传到Git仓库')

if __name__ == '__main__':
    main() 