from __future__ import annotations
import re
import pytest

# Corrected import statement to match the directory structure
from sorts.natural_sort import alphanum_key  # Import the function to be tested

class Test_NaturalSortAlphanumKey:

    @pytest.mark.positive
    def test_alphanum_key_mixed_content(self):
        # Arrange
        input_string = "File10Version2"
        expected_output = ['file', 10, 'version', 2]
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

    @pytest.mark.positive
    def test_alphanum_key_leading_zeros(self):
        # Arrange
        input_string = "Item007"
        expected_output = ['item', 7]
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

    @pytest.mark.positive
    def test_alphanum_key_only_alphabetic(self):
        # Arrange
        input_string = "HelloWorld"
        expected_output = ['helloworld']
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

    @pytest.mark.positive
    def test_alphanum_key_only_numeric(self):
        # Arrange
        input_string = "12345"
        expected_output = [12345]
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

    @pytest.mark.positive
    def test_alphanum_key_empty_string(self):
        # Arrange
        input_string = ""
        expected_output = []
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

    @pytest.mark.positive
    def test_alphanum_key_special_characters(self):
        # Arrange
        input_string = "File#1"
        expected_output = ['file#', 1]
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

    @pytest.mark.positive
    def test_alphanum_key_consecutive_numbers(self):
        # Arrange
        input_string = "Version1234"
        expected_output = ['version', 1234]
        
        # Act
        result = alphanum_key(input_string)
        
        # Assert
        assert result == expected_output

if __name__ == '__main__':
    import doctest
    doctest.testmod()
