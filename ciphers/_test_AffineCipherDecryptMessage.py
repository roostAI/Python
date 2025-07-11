import pytest
from affine_cipher import decrypt_message

class Test_AffineCipherDecryptMessage:

    @pytest.mark.regression
    def test_decrypt_valid_message(self):
        # Arrange
        key = 4545
        encrypted_message = 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
        expected_decrypted_message = 'The affine cipher is a type of monoalphabetic substitution cipher.'

        # Act
        decrypted_message = decrypt_message(key, encrypted_message)

        # Assert
        assert decrypted_message == expected_decrypted_message

    @pytest.mark.regression
    def test_decrypt_message_with_unknown_symbols(self):
        # Arrange
        key = 4545
        encrypted_message = 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi!!!'
        expected_decrypted_message = 'The affine cipher is a type of monoalphabetic substitution cipher.!!!'

        # Act
        decrypted_message = decrypt_message(key, encrypted_message)

        # Assert
        assert decrypted_message == expected_decrypted_message

    @pytest.mark.regression
    def test_decrypt_message_with_invalid_key(self):
        # Arrange
        key = -1
        encrypted_message = 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'

        # Act & Assert
        with pytest.raises(SystemExit):
            decrypt_message(key, encrypted_message)
