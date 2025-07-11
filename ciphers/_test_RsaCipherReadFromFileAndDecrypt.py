import os
import sys
import pytest
from rsa_cipher import read_from_file_and_decrypt

class Test_RsaCipherReadFromFileAndDecrypt:

    def test_read_from_file_and_decrypt_valid_files(self):
        # Arrange
        key_filename = 'valid_key.txt'
        message_filename = 'valid_message.txt'
        expected_message = 'Hello, World!'

        # Act
        result = read_from_file_and_decrypt(message_filename, key_filename)

        # Assert
        assert result == expected_message

    def test_read_from_file_and_decrypt_invalid_key_file(self):
        # Arrange
        key_filename = 'invalid_key.txt'
        message_filename = 'valid_message.txt'

        # Act & Assert
        with pytest.raises(Exception):
            read_from_file_and_decrypt(message_filename, key_filename)

    def test_read_from_file_and_decrypt_invalid_message_file(self):
        # Arrange
        key_filename = 'valid_key.txt'
        message_filename = 'invalid_message.txt'

        # Act & Assert
        with pytest.raises(Exception):
            read_from_file_and_decrypt(message_filename, key_filename)

    def test_read_from_file_and_decrypt_key_size_smaller_than_block_size(self):
        # Arrange
        key_filename = 'small_key.txt'
        message_filename = 'large_block_message.txt'

        # Act & Assert
        with pytest.raises(SystemExit):
            read_from_file_and_decrypt(message_filename, key_filename)
