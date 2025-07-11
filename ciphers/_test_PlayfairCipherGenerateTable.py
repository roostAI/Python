import pytest
from playfair_cipher import generate_table

class Test_PlayfairCipherGenerateTable:

    def test_generate_table_with_unique_characters(self):
        key = "HELLO"
        expected_table = ['H', 'E', 'L', 'O', 'A', 'B', 'C', 'D', 'F', 'G', 'I', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        assert generate_table(key) == expected_table

    def test_generate_table_with_duplicate_characters(self):
        key = "HELLOHELLO"
        expected_table = ['H', 'E', 'L', 'O', 'A', 'B', 'C', 'D', 'F', 'G', 'I', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        assert generate_table(key) == expected_table

    def test_generate_table_with_non_alphabet_characters(self):
        key = "HELLO123"
        expected_table = ['H', 'E', 'L', 'O', 'A', 'B', 'C', 'D', 'F', 'G', 'I', 'K', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        assert generate_table(key) == expected_table

    def test_generate_table_with_empty_key(self):
        key = ""
        expected_table = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        assert generate_table(key) == expected_table
