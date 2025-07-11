import pytest
import random
from permutation_cipher import main, encrypt, decrypt

class Test_PermutationCipherMain:

    @pytest.mark.regression
    def test_encryption_decryption_process(self):
        """
        Test Scenario 1: Testing the encryption and decryption process with a known message
        """
        message = "HELLO WORLD"
        encrypted_message, key = encrypt(message)
        decrypted_message = decrypt(encrypted_message, key)
        assert decrypted_message == message, "Decrypted message does not match the original message"

    @pytest.mark.regression
    def test_encryption_decryption_with_empty_message(self):
        """
        Test Scenario 2: Testing the encryption and decryption process with an empty message
        """
        message = ""
        encrypted_message, key = encrypt(message)
        decrypted_message = decrypt(encrypted_message, key)
        assert decrypted_message == message, "Decrypted message does not match the original message"

    @pytest.mark.regression
    def test_encryption_decryption_with_special_characters(self):
        """
        Test Scenario 3: Testing the encryption and decryption process with a message containing special characters
        """
        message = "!@#$%^&*()"
        encrypted_message, key = encrypt(message)
        decrypted_message = decrypt(encrypted_message, key)
        assert decrypted_message == message, "Decrypted message does not match the original message"
