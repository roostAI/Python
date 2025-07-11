import pytest
from transposition_cipher import encrypt_message

class Test_TranspositionCipherEncryptMessage:

    @pytest.mark.regression
    def test_encrypt_message_valid_key_and_message(self):
        # Act
        result = encrypt_message(6, 'Harshil Darji')
        # Assert
        assert result == 'Hlia rDsahrij', "The encryption result is not as expected"

    @pytest.mark.regression
    def test_encrypt_message_key_larger_than_message(self):
        # Act
        result = encrypt_message(20, 'Hello')
        # Assert
        assert result == 'Hello', "The encryption result is not as expected when key is larger than message"

    @pytest.mark.regression
    def test_encrypt_message_key_of_one(self):
        # Act
        result = encrypt_message(1, 'Hello')
        # Assert
        assert result == 'Hello', "The encryption result is not as expected when key is 1"
