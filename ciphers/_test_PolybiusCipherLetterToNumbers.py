import pytest
import numpy as np
from polybius import PolybiusCipher

class Test_PolybiusCipherLetterToNumbers:

    def test_letter_to_numbers_with_valid_letter(self):
        # Arrange
        cipher = PolybiusCipher()
        valid_letter = 'a'

        # Act
        result = cipher.letter_to_numbers(valid_letter)

        # Assert
        assert np.array_equal(result, [1,1])

    def test_letter_to_numbers_with_invalid_letter(self):
        # Arrange
        cipher = PolybiusCipher()
        invalid_letter = 'z'

        # Act and Assert
        with pytest.raises(ValueError):
            cipher.letter_to_numbers(invalid_letter)

    def test_letter_to_numbers_with_middle_letter(self):
        # Arrange
        cipher = PolybiusCipher()
        middle_letter = 'm'

        # Act
        result = cipher.letter_to_numbers(middle_letter)

        # Assert
        assert np.array_equal(result, [3,2])
