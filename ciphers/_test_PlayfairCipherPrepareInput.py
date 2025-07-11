import pytest
import string
from playfair_cipher import prepare_input

class Test_PlayfairCipherPrepareInput:

    def test_prepare_input_lowercase(self):
        input_str = 'hello'
        expected_output = 'HELXLOX'
        assert prepare_input(input_str) == expected_output

    def test_prepare_input_uppercase(self):
        input_str = 'HELLO'
        expected_output = 'HELXLOX'
        assert prepare_input(input_str) == expected_output

    def test_prepare_input_mixed_case(self):
        input_str = 'HeLLo'
        expected_output = 'HELXLOX'
        assert prepare_input(input_str) == expected_output

    def test_prepare_input_repeated_letters(self):
        input_str = 'aabbcc'
        expected_output = 'AAXBXBCXCX'
        assert prepare_input(input_str) == expected_output

    def test_prepare_input_non_letters(self):
        input_str = '123@#'
        expected_output = ''
        assert prepare_input(input_str) == expected_output

    def test_prepare_input_empty_string(self):
        input_str = ''
        expected_output = ''
        assert prepare_input(input_str) == expected_output
