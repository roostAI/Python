from __future__ import annotations
import doctest
import pytest
from diffie import find_primitive

class Test_DiffieFindPrimitive:

    @pytest.mark.regression
    def test_find_primitive_with_valid_modulus(self):
        # Act
        result = find_primitive(7)
        # Assert
        assert result == 3, "Expected primitive root for modulus 7 is 3"

    @pytest.mark.regression
    def test_find_primitive_with_invalid_modulus(self):
        # Act
        result = find_primitive(8)
        # Assert
        assert result is None, "Expected None for modulus 8 as it has no primitive root"

    @pytest.mark.regression
    def test_find_primitive_with_one_modulus(self):
        # Act
        result = find_primitive(1)
        # Assert
        assert result is None, "Expected None for modulus 1 as it has no primitive root"
