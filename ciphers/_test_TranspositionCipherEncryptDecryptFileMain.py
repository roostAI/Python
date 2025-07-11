import os
import sys
import time
import pytest
from unittest import mock
from transposition_cipher_encrypt_decrypt_file import main

class Test_TranspositionCipherEncryptDecryptFileMain:

    @pytest.mark.regression
    def test_input_file_does_not_exist(self, tmpdir):
        with mock.patch.object(sys, "exit") as mock_exit:
            with mock.patch.object(os.path, "exists", return_value=False):
                main()
        mock_exit.assert_called_once()

    @pytest.mark.regression
    def test_output_file_exists_no_overwrite(self, tmpdir):
        p = tmpdir.mkdir("sub").join("Output.txt")
        p.write("content")
        with mock.patch.object(sys, "exit") as mock_exit:
            with mock.patch.object(os.path, "exists", return_value=True):
                with mock.patch('builtins.input', side_effect=['n']):
                    main()
        mock_exit.assert_called_once()

    @pytest.mark.regression
    def test_encryption_mode(self, tmpdir):
        p = tmpdir.mkdir("sub").join("prehistoric_men.txt")
        p.write("content")
        with mock.patch.object(os.path, "exists", return_value=True):
            with mock.patch('builtins.input', side_effect=[3, 'e']):
                main()
        assert p.read() == "content"

    @pytest.mark.regression
    def test_decryption_mode(self, tmpdir):
        p = tmpdir.mkdir("sub").join("Output.txt")
        p.write("encrypted_content")
        with mock.patch.object(os.path, "exists", return_value=True):
            with mock.patch('builtins.input', side_effect=[3, 'd']):
                main()
        assert p.read() == "encrypted_content"
