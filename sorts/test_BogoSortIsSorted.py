# test_BogoSortIsSorted.py

import pytest
from sorts.bogo_sort import is_sorted

class Test_BogoSortIsSorted:

    @pytest.mark.positive
    def test_empty_list_is_sorted(self):
        # Arrange
        empty_list = []
        
        # Act
        result = is_sorted(empty_list)
        
        # Assert
        assert result is True

    @pytest.mark.positive
    def test_single_element_list_is_sorted(self):
        # Arrange
        single_element_list = [1]
        
        # Act
        result = is_sorted(single_element_list)
        
        # Assert
        assert result is True

    @pytest.mark.positive
    def test_ascending_order_list_is_sorted(self):
        # Arrange
        ascending_list = [1, 2, 3, 4, 5]
        
        # Act
        result = is_sorted(ascending_list)
        
        # Assert
        assert result is True

    @pytest.mark.negative
    def test_descending_order_list_is_not_sorted(self):
        # Arrange
        descending_list = [5, 4, 3, 2, 1]
        
        # Act
        result = is_sorted(descending_list)
        
        # Assert
        assert result is False

    @pytest.mark.positive
    def test_ascending_order_with_duplicates_is_sorted(self):
        # Arrange
        ascending_with_duplicates = [1, 2, 2, 3, 4]
        
        # Act
        result = is_sorted(ascending_with_duplicates)
        
        # Assert
        assert result is True

    @pytest.mark.negative
    def test_random_order_list_is_not_sorted(self):
        # Arrange
        random_order_list = [3, 1, 4, 2, 5]
        
        # Act
        result = is_sorted(random_order_list)
        
        # Assert
        assert result is False

    @pytest.mark.positive
    def test_identical_elements_list_is_sorted(self):
        # Arrange
        identical_elements_list = [2, 2, 2, 2]
        
        # Act
        result = is_sorted(identical_elements_list)
        
        # Assert
        assert result is True
