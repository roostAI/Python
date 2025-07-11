from __future__ import annotations
import pytest
from decrypt_caesar_with_chi_squared import chi_squared_statistic_values_sorting_key

class Test_DecryptCaesarWithChiSquaredChiSquaredStatisticValuesSortingKey:

    @pytest.mark.valid
    def test_chi_squared_statistic_values_sorting_key_valid_key(self):
        # Arrange
        chi_squared_statistic_values = {1: (2.5, 'a'), 2: (3.5, 'b'), 3: (4.5, 'c')}
        key = 2

        # Act
        result = chi_squared_statistic_values_sorting_key(key)

        # Assert
        assert result == chi_squared_statistic_values[key]

    @pytest.mark.invalid
    def test_chi_squared_statistic_values_sorting_key_invalid_key(self):
        # Arrange
        chi_squared_statistic_values = {1: (2.5, 'a'), 2: (3.5, 'b'), 3: (4.5, 'c')}
        key = 4

        # Act & Assert
        with pytest.raises(KeyError):
            chi_squared_statistic_values_sorting_key(key)

    @pytest.mark.negative
    def test_chi_squared_statistic_values_sorting_key_empty_dictionary(self):
        # Arrange
        chi_squared_statistic_values = {}
        key = 1

        # Act & Assert
        with pytest.raises(KeyError):
            chi_squared_statistic_values_sorting_key(key)
