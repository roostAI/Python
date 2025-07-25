# Corrected test_MergeSortMerge.py

import pytest
from sorts.merge_sort import merge  # Corrected import statement
import doctest

class Test_MergeSortMerge:

    @pytest.mark.positive
    def test_merge_two_non_empty_sorted_lists(self):
        # Arrange
        left = [1, 3, 5]
        right = [2, 4, 6]
        
        # Act
        result = merge(left, right)
        
        # Assert
        assert result == [1, 2, 3, 4, 5, 6]

    @pytest.mark.positive
    def test_merge_with_one_empty_list(self):
        # Arrange
        left = [1, 2, 3]
        right = []
        
        # Act
        result = merge(left, right)
        
        # Assert
        assert result == [1, 2, 3]

    @pytest.mark.positive
    def test_merge_two_empty_lists(self):
        # Arrange
        left = []
        right = []
        
        # Act
        result = merge(left, right)
        
        # Assert
        assert result == []

    @pytest.mark.positive
    def test_merge_lists_with_duplicates(self):
        # Arrange
        left = [1, 2, 2, 3]
        right = [2, 3, 4]
        
        # Act
        result = merge(left, right)
        
        # Assert
        assert result == [1, 2, 2, 2, 3, 3, 4]

    @pytest.mark.positive
    def test_merge_lists_with_negative_numbers(self):
        # Arrange
        left = [-3, -1, 0]
        right = [-2, 1, 2]
        
        # Act
        result = merge(left, right)
        
        # Assert
        assert result == [-3, -2, -1, 0, 1, 2]

    @pytest.mark.positive
    def test_merge_lists_with_different_lengths(self):
        # Arrange
        left = [1, 4, 5]
        right = [2]
        
        # Act
        result = merge(left, right)
        
        # Assert
        assert result == [1, 2, 4, 5]

if __name__ == '__main__':
    doctest.testmod()
    pytest.main()
