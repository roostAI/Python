import pytest
from a1z26 import main, encode, decode

class Test_A1Z26Main:

    @pytest.mark.regression
    def test_encode_decode_simple_string(self):
        # Arrange
        input_string = "hello"
        expected_output = input_string

        # Act
        encoded = encode(input_string)
        decoded = decode(encoded)

        # Assert
        assert decoded == expected_output, f"For input {input_string}, expected output is {expected_output} but got {decoded}"

    @pytest.mark.regression
    def test_encode_decode_special_chars(self):
        # Arrange
        input_string = "hello@world"
        expected_output = input_string

        # Act
        encoded = encode(input_string)
        decoded = decode(encoded)

        # Assert
        assert decoded == expected_output, f"For input {input_string}, expected output is {expected_output} but got {decoded}"

    @pytest.mark.regression
    def test_encode_decode_empty_string(self):
        # Arrange
        input_string = ""
        expected_output = input_string

        # Act
        encoded = encode(input_string)
        decoded = decode(encoded)

        # Assert
        assert decoded == expected_output, f"For input {input_string}, expected output is {expected_output} but got {decoded}"
