import pytest
from affine_cipher import main

class Test_AffineCipherMain:
    @pytest.mark.positive
    def test_main_encrypt_mode(self):
        # Arrange
        message = "This is a test!"
        key = 2000
        mode = "e"

        # Act
        result = main(message, key, mode)

        # Assert
        assert result != message, "The message should be encrypted"

    @pytest.mark.positive
    def test_main_decrypt_mode(self):
        # Arrange
        message = "This is a test!"
        key = 2000
        mode = "e"
        encrypted_message = main(message, key, mode)

        mode = "d"

        # Act
        result = main(encrypted_message, key, mode)

        # Assert
        assert result == message, "The message should be decrypted"

    @pytest.mark.negative
    def test_main_invalid_mode(self):
        # Arrange
        message = "This is a test!"
        key = 2000
        mode = "invalid"

        # Act and Assert
        with pytest.raises(ValueError):
            main(message, key, mode)

    @pytest.mark.negative
    def test_main_invalid_key(self):
        # Arrange
        message = "This is a test!"
        key = -1
        mode = "e"

        # Act and Assert
        with pytest.raises(ValueError):
            main(message, key, mode)
