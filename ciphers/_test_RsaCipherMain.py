import os
import sys
import pytest
from unittest.mock import patch
from rsa_cipher import main

class Test_RsaCipherMain:
    @pytest.mark.positive
    def test_encryption_process(self):
        with patch('builtins.input', side_effect=['e', 'Test Message']):
            main()
            with open('encrypted_file.txt', 'r') as f:
                encrypted_text = f.read()
            assert encrypted_text is not None
            assert encrypted_text != 'Test Message'

    @pytest.mark.positive
    def test_decryption_process(self):
        with patch('builtins.input', side_effect=['d']):
            main()
            with open('rsa_decryption.txt', 'r') as f:
                decrypted_text = f.read()
            assert decrypted_text is not None
            assert decrypted_text == 'Test Message'

    @pytest.mark.negative
    def test_invalid_response(self):
        with patch('builtins.input', side_effect=['invalid']):
            main()
            assert not os.path.exists('encrypted_file.txt')
            assert not os.path.exists('rsa_decryption.txt')
