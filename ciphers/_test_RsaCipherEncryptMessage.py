import os
import sys
import pytest
from rsa_cipher import encrypt_message, DEFAULT_BLOCK_SIZE

class Test_RsaCipherEncryptMessage:

    @pytest.mark.valid
    def test_encrypt_message_with_valid_inputs(self):
        # Arrange
        message = "Hello, World!"
        key = (3233, 17)  # Public key
        block_size = DEFAULT_BLOCK_SIZE
        expected_encrypted_blocks = [pow(block, key[1], key[0]) for block in get_blocks_from_text(message, block_size)]

        # Act
        actual_encrypted_blocks = encrypt_message(message, key, block_size)

        # Assert
        assert actual_encrypted_blocks == expected_encrypted_blocks

    @pytest.mark.edge
    def test_encrypt_message_with_empty_message(self):
        # Arrange
        message = ""
        key = (3233, 17)  # Public key
        block_size = DEFAULT_BLOCK_SIZE
        expected_encrypted_blocks = []

        # Act
        actual_encrypted_blocks = encrypt_message(message, key, block_size)

        # Assert
        assert actual_encrypted_blocks == expected_encrypted_blocks

    @pytest.mark.performance
    def test_encrypt_message_with_large_message(self):
        # Arrange
        message = "A" * 10000  # Large message
        key = (3233, 17)  # Public key
        block_size = DEFAULT_BLOCK_SIZE
        expected_encrypted_blocks = [pow(block, key[1], key[0]) for block in get_blocks_from_text(message, block_size)]

        # Act
        actual_encrypted_blocks = encrypt_message(message, key, block_size)

        # Assert
        assert actual_encrypted_blocks == expected_encrypted_blocks
