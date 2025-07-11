from __future__ import annotations
import pytest
from a1z26 import decode

class Test_A1Z26Decode:
    @pytest.mark.valid
    def test_decode_with_valid_input(self):
        # Arrange
        valid_input = [13, 25, 14, 1, 13, 5]
        expected_output = 'myname'

        # Act
        actual_output = decode(valid_input)

        # Assert
        assert actual_output == expected_output, f"For valid input, expected {expected_output} but got {actual_output}"

    @pytest.mark.valid
    def test_decode_with_empty_list(self):
        # Arrange
        empty_list = []
        expected_output = ''

        # Act
        actual_output = decode(empty_list)

        # Assert
        assert actual_output == expected_output, f"For empty list, expected {expected_output} but got {actual_output}"

    @pytest.mark.invalid
    def test_decode_with_out_of_range_input(self):
        # Arrange
        out_of_range_input = [27, 28, 0, -1]
        expected_output = '{|~'

        # Act
        actual_output = decode(out_of_range_input)

        # Assert
        assert actual_output == expected_output, f"For out of range input, expected {expected_output} but got {actual_output}"

    @pytest.mark.invalid
    def test_decode_with_zero_input(self):
        # Arrange
        zero_input = [0]
        expected_output = '`'

        # Act
        actual_output = decode(zero_input)

        # Assert
        assert actual_output == expected_output, f"For zero input, expected {expected_output} but got {actual_output}"
