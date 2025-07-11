import pytest
from playfair_cipher import encode

class Test_PlayfairCipherEncode:

    def test_encode_valid_input(self):
        plaintext = "Hello"
        key = "MONARCHY"
        expected_output = "CFSUPM"
        assert encode(plaintext, key) == expected_output

    def test_encode_empty_plaintext(self):
        plaintext = ""
        key = "MONARCHY"
        expected_output = ""
        assert encode(plaintext, key) == expected_output

    def test_encode_special_characters(self):
        plaintext = "Hello!"
        key = "MONARCHY"
        expected_output = "CFSUPM"
        assert encode(plaintext, key) == expected_output

    def test_encode_numbers(self):
        plaintext = "Hello1"
        key = "MONARCHY"
        expected_output = "CFSUPM"
        assert encode(plaintext, key) == expected_output

    def test_encode_empty_key(self):
        plaintext = "Hello"
        key = ""
        expected_output = "CFSUPM"
        assert encode(plaintext, key) == expected_output
