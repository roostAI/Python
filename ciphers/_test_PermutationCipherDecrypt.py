import pytest
from permutation_cipher import decrypt

class Test_PermutationCipherDecrypt:

    @pytest.mark.positive
    def test_decrypt_valid_input(self):
        # Arrange
        encrypted_message = "EHLLOD LORW"
        key = [1, 0, 2, 4, 3]

        # Act
        result = decrypt(encrypted_message, key)

        # Assert
        assert result == "HELLO WORLD"

    @pytest.mark.negative
    def test_decrypt_empty_string(self):
        # Arrange
        encrypted_message = ""
        key = [1, 0, 2, 4, 3]

        # Act
        result = decrypt(encrypted_message, key)

        # Assert
        assert result == ""

    @pytest.mark.edge
    def test_decrypt_key_length_one(self):
        # Arrange
        encrypted_message = "HELLO WORLD"
        key = [0]

        # Act
        result = decrypt(encrypted_message, key)

        # Assert
        assert result == "HELLO WORLD"
