import pytest
import random
from affine_cipher import get_random_key
from maths.greatest_common_divisor import gcd_by_iterative

class Test_AffineCipherGetRandomKey:

    @pytest.mark.regression
    def test_return_type(self):
        # Act
        result = get_random_key()
        # Assert
        assert isinstance(result, int), "The return type should be an integer"

    @pytest.mark.regression
    def test_return_value(self):
        # Act
        result = get_random_key()
        # Assert
        assert result > 0, "The return value should be a positive integer"

    @pytest.mark.regression
    def test_return_uniqueness(self):
        # Act
        result1 = get_random_key()
        result2 = get_random_key()
        # Assert
        assert result1 != result2, "The function should return a unique value each time it is called"
