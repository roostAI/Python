import pytest
from caesar_cipher import encrypt
from string import ascii_letters

class Test_CaesarCipherEncrypt:

    def test_encrypt_with_default_alphabet_and_positive_key(self):
        assert encrypt('Hello, world!', 3) == 'Khoor, zruog!'

    def test_encrypt_with_default_alphabet_and_negative_key(self):
        assert encrypt('Khoor, zruog!', -3) == 'Hello, world!'

    def test_encrypt_with_custom_alphabet_and_positive_key(self):
        custom_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        assert encrypt('Hello, world!', 3, custom_alphabet) == 'Khoor, zruog!'

    def test_encrypt_with_custom_alphabet_and_negative_key(self):
        custom_alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        assert encrypt('Khoor, zruog!', -3, custom_alphabet) == 'Hello, world!'

    def test_encrypt_with_non_alphabet_characters(self):
        assert encrypt('Hello, world!', 3) == 'Khoor, zruog!'
