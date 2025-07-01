import os
import sys
import pyperclip
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from common.compress_util import decompress_text
from common.crypto_util import decrypt

GIT_FILE = 'clipboard.enc'

def main():
    password = os.environ.get('CLIPBOARD_PASS')
    workdir = os.environ.get('CLIPBOARD_WORKDIR')
    if not password:
        print('请先设置环境变量CLIPBOARD_PASS')
        return
    if not workdir:
        print('请先设置环境变量CLIPBOARD_WORKDIR为git仓库本地路径')
        return
    if not os.path.isdir(workdir):
        print(f'指定的工作目录不存在: {workdir}')
        return
    os.chdir(workdir)
    # git pull 拉取最新内容
    os.system('git pull')
    if not os.path.exists(GIT_FILE):
        print(f'未找到加密文件: {GIT_FILE}')
        return
    with open(GIT_FILE, 'rb') as f:
        encrypted = f.read()
    try:
        decrypted = decrypt(encrypted, password)
        text = decompress_text(decrypted)
    except Exception as e:
        print('解密或解压失败，可能是密码错误或文件损坏')
        return
    try:
        pyperclip.copy(text)
        print('内容已写入本地剪切板')
    except pyperclip.PyperclipException:
        with open('output.txt', 'w', encoding='utf-8') as f:
            f.write(text)
        print('无法写入剪切板，内容已输出到output.txt')

if __name__ == '__main__':
    main() 