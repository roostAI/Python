import pytest
from rsa_cipher import decrypt_message

class Test_RsaCipherDecryptMessage:
    @pytest.mark.positive
    def test_decrypt_message_with_valid_input(self):
        # Arrange
        encrypted_blocks = [123, 456, 789]
        message_length = 3
        key = (123, 456)
        expected_decrypted_message = "abc"

        # Act
        result = decrypt_message(encrypted_blocks, message_length, key)

        # Assert
        assert result == expected_decrypted_message, "The decrypted message does not match the expected output"

    @pytest.mark.negative
    def test_decrypt_message_with_empty_input(self):
        # Arrange
        encrypted_blocks = []
        message_length = 0
        key = (123, 456)
        expected_decrypted_message = ""

        # Act
        result = decrypt_message(encrypted_blocks, message_length, key)

        # Assert
        assert result == expected_decrypted_message, "The decrypted message does not match the expected output"

    @pytest.mark.negative
    def test_decrypt_message_with_invalid_key(self):
        # Arrange
        encrypted_blocks = [123, 456, 789]
        message_length = 3
        key = ("invalid", "key")

        # Act and Assert
        with pytest.raises(TypeError):
            decrypt_message(encrypted_blocks, message_length, key)
