import pytest
import numpy as np
from polybius import PolybiusCipher

class Test_PolybiusCipherNumbersToLetter:

    @pytest.mark.positive
    def test_numbers_to_letter_valid_indices(self):
        # Arrange
        cipher = PolybiusCipher()
        # Act
        result = cipher.numbers_to_letter(1, 1)
        # Assert
        assert result == "a", "The function did not return the expected result for valid indices."

    @pytest.mark.negative
    def test_numbers_to_letter_invalid_indices(self):
        # Arrange
        cipher = PolybiusCipher()
        # Act and Assert
        with pytest.raises(IndexError, match="Index out of range"):
            cipher.numbers_to_letter(6, 6)

    @pytest.mark.negative
    def test_numbers_to_letter_non_integer_indices(self):
        # Arrange
        cipher = PolybiusCipher()
        # Act and Assert
        with pytest.raises(TypeError, match="Indices must be integers"):
            cipher.numbers_to_letter(1.5, 2.5)
