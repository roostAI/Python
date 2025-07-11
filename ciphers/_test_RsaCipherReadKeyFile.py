import os
import sys
import pytest
from rsa_cipher import read_key_file

class Test_RsaCipherReadKeyFile:

    @pytest.mark.valid
    def test_read_key_file_with_valid_file(self):
        # Arrange
        key_filename = 'valid_key_file.txt'
        with open(key_filename, 'w') as f:
            f.write('1024,1234567890,9876543210')
        expected_output = (1024, 1234567890, 9876543210)

        # Act
        output = read_key_file(key_filename)

        # Assert
        assert output == expected_output

        # Cleanup
        os.remove(key_filename)

    @pytest.mark.invalid
    def test_read_key_file_with_invalid_file(self):
        # Arrange
        key_filename = 'invalid_key_file.txt'
        with open(key_filename, 'w') as f:
            f.write('1024,1234567890,invalid')

        # Act & Assert
        with pytest.raises(ValueError):
            read_key_file(key_filename)

        # Cleanup
        os.remove(key_filename)

    @pytest.mark.negative
    def test_read_key_file_with_non_existent_file(self):
        # Arrange
        key_filename = 'non_existent_file.txt'

        # Act & Assert
        with pytest.raises(FileNotFoundError):
            read_key_file(key_filename)

    @pytest.mark.invalid
    def test_read_key_file_with_extra_data(self):
        # Arrange
        key_filename = 'extra_data_key_file.txt'
        with open(key_filename, 'w') as f:
            f.write('1024,1234567890,9876543210,extra')

        # Act & Assert
        with pytest.raises(ValueError):
            read_key_file(key_filename)

        # Cleanup
        os.remove(key_filename)
