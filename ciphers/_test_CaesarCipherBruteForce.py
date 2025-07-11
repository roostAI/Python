import pytest
from caesar_cipher import brute_force
from string import ascii_letters

class Test_CaesarCipherBruteForce:

    @pytest.mark.regression
    def test_brute_force_with_valid_cipher_text(self):
        cipher_text = "jFyuMy xIH'N vLONy zILwy Gy!"
        result = brute_force(cipher_text)
        assert len(result) == len(ascii_letters)
        assert all(isinstance(value, str) for value in result.values())

    @pytest.mark.regression
    def test_brute_force_with_custom_alphabet(self):
        cipher_text = "jFyuMy xIH'N vLONy zILwy Gy!"
        custom_alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
        result = brute_force(cipher_text, custom_alphabet)
        assert len(result) == len(custom_alphabet)
        assert all(isinstance(value, str) for value in result.values())

    @pytest.mark.negative
    def test_brute_force_with_invalid_cipher_text(self):
        invalid_cipher_text = 123
        with pytest.raises(TypeError):
            brute_force(invalid_cipher_text)

    @pytest.mark.edge
    def test_brute_force_with_empty_cipher_text(self):
        empty_cipher_text = ""
        result = brute_force(empty_cipher_text)
        assert result == {}
