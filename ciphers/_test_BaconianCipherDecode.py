import pytest
from baconian_cipher import decode

class Test_BaconianCipherDecode:

    @pytest.mark.positive
    def test_decode_valid_input(self):
        # Arrange
        valid_input = "AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB"
        expected_output = "hello world"

        # Act
        actual_output = decode(valid_input)

        # Assert
        assert actual_output == expected_output, "Decoding of valid input failed"

    @pytest.mark.negative
    def test_decode_invalid_input(self):
        # Arrange
        invalid_input = "AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB!"

        # Act & Assert
        with pytest.raises(Exception) as e:
            decode(invalid_input)
        assert str(e.value) == "decode() accepts only 'A', 'B' and spaces", "Exception not raised for invalid input"

    @pytest.mark.edge
    def test_decode_empty_string(self):
        # Arrange
        empty_input = ""
        expected_output = ""

        # Act
        actual_output = decode(empty_input)

        # Assert
        assert actual_output == expected_output, "Decoding of empty string failed"

    @pytest.mark.positive
    def test_decode_extra_spaces(self):
        # Arrange
        input_with_extra_spaces = " AABBBAABAAABABAABABAABBAB  BABAAABBABBAAAAABABAAAABB "
        expected_output = "hello world"

        # Act
        actual_output = decode(input_with_extra_spaces)

        # Assert
        assert actual_output == expected_output, "Decoding of string with extra spaces failed"
