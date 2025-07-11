import pytest
from permutation_cipher import encrypt

class Test_PermutationCipherEncrypt:

    @pytest.mark.positive
    def test_encrypt_with_key_and_block_size(self):
        message = "HELLO WORLD"
        key = [2, 0, 1, 3]
        block_size = 4
        expected_encrypted_message = "LEH OLWLODR"
        encrypted_message, returned_key = encrypt(message, key, block_size)
        assert encrypted_message == expected_encrypted_message
        assert returned_key == key

    @pytest.mark.positive
    def test_encrypt_without_key_and_block_size(self):
        message = "HELLO WORLD"
        encrypted_message, key = encrypt(message)
        assert len(encrypted_message) == len(message)
        assert isinstance(key, list)
        assert len(key) > 0

    @pytest.mark.negative
    def test_encrypt_empty_message(self):
        message = ""
        expected_encrypted_message = ""
        expected_key = None
        encrypted_message, key = encrypt(message)
        assert encrypted_message == expected_encrypted_message
        assert key == expected_key

    @pytest.mark.negative
    def test_encrypt_large_block_size(self):
        message = "HELLO WORLD"
        block_size = len(message) + 1
        with pytest.raises(ValueError):
            encrypt(message, block_size=block_size)
