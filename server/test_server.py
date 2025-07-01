import pytest
from unittest.mock import patch, mock_open
import server

@patch('os.system')
@patch('builtins.open', new_callable=mock_open)
@patch('pyperclip.paste', return_value='test content')
@patch.dict('os.environ', {'CLIPBOARD_PASS': '123456'})
def test_main_success(mock_clip, mock_file, mock_system):
    server.main()
    mock_file.assert_called_with('clipboard.enc', 'wb')
    assert mock_system.called

@patch('pyperclip.paste', return_value='')
@patch.dict('os.environ', {'CLIPBOARD_PASS': '123456'})
def test_main_clipboard_empty(mock_clip):
    with patch('builtins.print') as mock_print:
        server.main()
        mock_print.assert_any_call('剪切板为空')

@patch('pyperclip.paste', return_value='test')
@patch.dict('os.environ', {})
def test_main_no_password(mock_clip):
    with patch('builtins.print') as mock_print:
        server.main()
        mock_print.assert_any_call('请先设置环境变量CLIPBOARD_PASS') 