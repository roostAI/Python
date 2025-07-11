import os
import sys
import pytest
from rsa_cipher import encrypt_and_write_to_file

class Test_RsaCipherEncryptAndWriteToFile:

    @pytest.mark.negative
    def test_block_size_greater_than_key_size(self, monkeypatch):
        def mock_exit(*args, **kwargs):
            raise SystemExit(args[0])
        monkeypatch.setattr(sys, 'exit', mock_exit)

        with pytest.raises(SystemExit) as pytest_wrapped_e:
            encrypt_and_write_to_file('message.txt', 'small_key.txt', 'Hello, World!', 2048)
        assert pytest_wrapped_e.type == SystemExit
        assert pytest_wrapped_e.value.args[0] == "ERROR: Block size is 16384 bits and key size is 1024 bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys."

    @pytest.mark.positive
    def test_successful_encryption_and_file_write(self):
        encrypted_content = encrypt_and_write_to_file('message.txt', 'key.txt', 'Hello, World!', 128)
        with open('message.txt', 'r') as fo:
            file_content = fo.read()
        assert encrypted_content == file_content

    @pytest.mark.positive
    def test_encryption_with_different_block_sizes(self):
        for block_size in [64, 128, 256, 512]:
            encrypted_content = encrypt_and_write_to_file('message.txt', 'key.txt', 'Hello, World!', block_size)
            with open('message.txt', 'r') as fo:
                file_content = fo.read()
            assert encrypted_content == file_content

    @pytest.mark.negative
    def test_encryption_with_empty_message(self):
        encrypted_content = encrypt_and_write_to_file('message.txt', 'key.txt', '', 128)
        with open('message.txt', 'r') as fo:
            file_content = fo.read()
        assert encrypted_content == file_content
        assert encrypted_content == '0_128_'
