# Corrected test_CircleSortCircleSortUtil.py

import pytest
from circle_sort import circle_sort_util

class TestCircleSortUtil:

    @pytest.mark.positive
    def test_correct_swapping_of_elements(self):
        # Arrange
        test_list = [5, 4, 3, 2, 1]
        expected_result = [1, 4, 3, 2, 5]
        
        # Act
        circle_sort_util(test_list, 0, 4)
        
        # Assert
        assert test_list == expected_result

    @pytest.mark.positive
    def test_no_swapping_when_sorted(self):
        # Arrange
        test_list = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        
        # Act
        result = circle_sort_util(test_list, 0, 4)
        
        # Assert
        assert test_list == expected_result
        assert result is False

    @pytest.mark.positive
    def test_single_element_range(self):
        # Arrange
        test_list = [3, 1, 4, 1, 5]
        expected_result = [3, 1, 4, 1, 5]
        
        # Act
        result = circle_sort_util(test_list, 2, 2)
        
        # Assert
        assert test_list == expected_result
        assert result is False

    @pytest.mark.positive
    def test_recursive_sorting_of_subarrays(self):
        # Arrange
        test_list = [5, 3, 4, 1, 2]
        expected_result = [1, 2, 3, 4, 5]
        
        # Act
        circle_sort_util(test_list, 0, 4)
        
        # Assert
        assert test_list == expected_result

    @pytest.mark.positive
    def test_odd_length_array(self):
        # Arrange
        test_list = [7, 3, 5, 1, 9]
        expected_result = [1, 3, 5, 7, 9]
        
        # Act
        circle_sort_util(test_list, 0, 4)
        
        # Assert
        assert test_list == expected_result

    @pytest.mark.positive
    def test_even_length_array(self):
        # Arrange
        test_list = [8, 4, 6, 2]
        expected_result = [2, 4, 6, 8]
        
        # Act
        circle_sort_util(test_list, 0, 3)
        
        # Assert
        assert test_list == expected_result
