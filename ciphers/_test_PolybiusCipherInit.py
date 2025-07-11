import pytest
import numpy as np
from polybius import PolybiusCipher

class Test_PolybiusCipherInit:
    @pytest.mark.regression
    def test_initialization_of_square(self):
        # Arrange
        cipher = PolybiusCipher()
        expected_square = np.array([
            ["a", "b", "c", "d", "e"],
            ["f", "g", "h", "i", "k"],
            ["l", "m", "n", "o", "p"],
            ["q", "r", "s", "t", "u"],
            ["v", "w", "x", "y", "z"],
        ])

        # Act
        # No action is required as the attribute is initialized during instantiation.

        # Assert
        assert np.array_equal(cipher.SQUARE, expected_square)

    @pytest.mark.regression
    def test_square_attribute_type(self):
        # Arrange
        cipher = PolybiusCipher()

        # Act
        # No action is required as the attribute is initialized during instantiation.

        # Assert
        assert isinstance(cipher.SQUARE, np.ndarray)

    @pytest.mark.regression
    def test_square_attribute_shape(self):
        # Arrange
        cipher = PolybiusCipher()

        # Act
        # No action is required as the attribute is initialized during instantiation.

        # Assert
        assert cipher.SQUARE.shape == (5, 5)
