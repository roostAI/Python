import pytest
import math
from transposition_cipher import decrypt_message

class Test_TranspositionCipherDecryptMessage:

    def test_decrypt_message_valid_key_and_message(self):
        key = 6
        message = 'Hlia rDsahrij'
        expected_output = 'Harshil Darji'
        assert decrypt_message(key, message) == expected_output

    def test_decrypt_message_key_larger_than_message(self):
        key = 20
        message = 'Hlia rDsahrij'
        expected_output = 'Hlia rDsahrij'
        assert decrypt_message(key, message) == expected_output

    def test_decrypt_message_key_equal_to_message_length(self):
        key = 13
        message = 'Hlia rDsahrij'
        expected_output = 'Hlia rDsahrij'
        assert decrypt_message(key, message) == expected_output

    def test_decrypt_message_empty_message(self):
        key = 6
        message = ''
        expected_output = ''
        assert decrypt_message(key, message) == expected_output
