from __future__ import annotations
import pytest
from a1z26 import encode

class Test_A1Z26Encode:

    def test_encode_with_simple_string(self):
        result = encode("abc")
        assert result == [1, 2, 3], "The function failed to encode a simple string correctly."

    def test_encode_with_uppercase_letters(self):
        result = encode("ABC")
        assert result == [-31, -30, -29], "The function failed to handle uppercase letters correctly."

    def test_encode_with_special_characters(self):
        result = encode("@#%")
        assert result == [-48, -35, -13], "The function failed to handle special characters correctly."

    def test_encode_with_empty_string(self):
        result = encode("")
        assert result == [], "The function failed to handle an empty string correctly."
