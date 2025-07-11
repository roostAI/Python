import pytest
from rsa_cipher import get_blocks_from_text, DEFAULT_BLOCK_SIZE, BYTE_SIZE

class Test_RsaCipherGetBlocksFromText:

    def test_get_blocks_from_text_with_simple_string(self):
        # Arrange
        simple_string = "Hello, World!"
        expected_output = [sum(ord(c) * (BYTE_SIZE ** i) for i, c in enumerate(simple_string))]

        # Act
        output = get_blocks_from_text(simple_string)

        # Assert
        assert output == expected_output

    def test_get_blocks_from_text_with_complex_string(self):
        # Arrange
        complex_string = "Hello, World! This is a complex string with special characters like @#$%^&*()_+"
        custom_block_size = 64
        expected_output = [sum(ord(c) * (BYTE_SIZE ** i) for i, c in enumerate(complex_string[j:j+custom_block_size])) for j in range(0, len(complex_string), custom_block_size)]

        # Act
        output = get_blocks_from_text(complex_string, custom_block_size)

        # Assert
        assert output == expected_output

    def test_get_blocks_from_text_with_empty_string(self):
        # Arrange
        empty_string = ""

        # Act
        output = get_blocks_from_text(empty_string)

        # Assert
        assert output == []

    def test_get_blocks_from_text_with_non_ascii_string(self):
        # Arrange
        non_ascii_string = "Hello, 世界!"

        # Act & Assert
        with pytest.raises(UnicodeEncodeError):
            get_blocks_from_text(non_ascii_string)
