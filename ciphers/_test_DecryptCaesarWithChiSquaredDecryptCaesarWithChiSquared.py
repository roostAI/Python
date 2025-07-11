from __future__ import annotations
import pytest
from decrypt_caesar_with_chi_squared import decrypt_caesar_with_chi_squared

class Test_DecryptCaesarWithChiSquaredDecryptCaesarWithChiSquared:
    
    @pytest.mark.regression
    def test_decrypt_caesar_with_chi_squared_simple_text(self):
        ciphertext = 'ifmmp'
        expected_result = (1, 0.0, 'hello')
        result = decrypt_caesar_with_chi_squared(ciphertext)
        assert result == expected_result, f"For {ciphertext}, expected {expected_result} but got {result}"

    @pytest.mark.regression
    def test_decrypt_caesar_with_chi_squared_complex_text(self):
        ciphertext = 'jg zpv epo\'u lopx, zpv dbo\'u hfu jo!'
        expected_result = (1, 0.0, 'if you don\'t know, you can\'t get in!')
        result = decrypt_caesar_with_chi_squared(ciphertext)
        assert result == expected_result, f"For {ciphertext}, expected {expected_result} but got {result}"

    @pytest.mark.regression
    def test_decrypt_caesar_with_chi_squared_case_sensitivity(self):
        ciphertext = 'Ifmmp'
        expected_result = (1, 0.0, 'Hello')
        result = decrypt_caesar_with_chi_squared(ciphertext, case_sensitive=True)
        assert result == expected_result, f"For {ciphertext}, expected {expected_result} but got {result}"

    @pytest.mark.regression
    def test_decrypt_caesar_with_chi_squared_custom_alphabet(self):
        ciphertext = 'jgnnq'
        custom_alphabet = [chr(i) for i in range(97, 123)] + [chr(i) for i in range(65, 91)]
        expected_result = (2, 0.0, 'hello')
        result = decrypt_caesar_with_chi_squared(ciphertext, cipher_alphabet=custom_alphabet)
        assert result == expected_result, f"For {ciphertext}, expected {expected_result} but got {result}"

    @pytest.mark.regression
    def test_decrypt_caesar_with_chi_squared_custom_frequencies(self):
        ciphertext = 'jgnnq'
        custom_frequencies = {
            "a": 0.08497,
            "b": 0.01492,
            "c": 0.02202,
            "d": 0.04253,
            "e": 0.11162,
            "f": 0.02228,
            "g": 0.02015,
            "h": 0.06094,
            "i": 0.07546,
            "j": 0.00153,
            "k": 0.01292,
            "l": 0.04025,
            "m": 0.02406,
            "n": 0.06749,
            "o": 0.07507,
            "p": 0.01929,
            "q": 0.00095,
            "r": 0.07587,
            "s": 0.06327,
            "t": 0.09356,
            "u": 0.02758,
            "v": 0.00978,
            "w": 0.02560,
            "x": 0.00150,
            "y": 0.01994,
            "z": 0.00077,
        }
        expected_result = (2, 0.0, 'hello')
        result = decrypt_caesar_with_chi_squared(ciphertext, frequencies_dict=custom_frequencies)
        assert result == expected_result, f"For {ciphertext}, expected {expected_result} but got {result}"
