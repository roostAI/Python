from __future__ import annotations
from string import ascii_letters
import pytest
from caesar_cipher import decrypt

class Test_CaesarCipherDecrypt:
    def test_decrypt_positive_key_default_alphabet(self):
        input_string = 'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'
        key = 8
        expected_output = 'The quick brown fox jumps over the lazy dog'
        assert decrypt(input_string, key) == expected_output

    def test_decrypt_negative_key_default_alphabet(self):
        input_string = 'The quick brown fox jumps over the lazy dog'
        key = -8
        expected_output = 'bpm yCqks jzwEv nwF rCuxA wDmz Bpm tiHG lwo'
        assert decrypt(input_string, key) == expected_output

    def test_decrypt_positive_key_custom_alphabet(self):
        input_string = 'f qtbjwhfxj fqumfgjy'
        key = 5
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        expected_output = 'a lowercase alphabet'
        assert decrypt(input_string, key, alphabet) == expected_output

    def test_decrypt_negative_key_custom_alphabet(self):
        input_string = 'a lowercase alphabet'
        key = -5
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        expected_output = 'f qtbjwhfxj fqumfgjy'
        assert decrypt(input_string, key, alphabet) == expected_output

    def test_decrypt_large_key(self):
        input_string = 'A very large key'
        key = 8000
        expected_output = 's nWjq dSjYW cWq'
        assert decrypt(input_string, key) == expected_output
