import pytest
from cryptomath_module import find_mod_inverse
from maths.greatest_common_divisor import gcd_by_iterative

class Test_CryptomathModuleFindModInverse:

    @pytest.mark.positive
    def test_find_mod_inverse_valid_inputs(self):
        # Arrange
        a, m = 3, 7  # gcd(3, 7) = 1
        expected_result = 5  # 5 is the modular inverse of 3 modulo 7

        # Act
        result = find_mod_inverse(a, m)

        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.negative
    def test_find_mod_inverse_invalid_inputs(self):
        # Arrange
        a, m = 4, 8  # gcd(4, 8) != 1

        # Act & Assert
        with pytest.raises(ValueError) as e:
            find_mod_inverse(a, m)
        assert str(e.value) == f"mod inverse of {a!r} and {m!r} does not exist", "ValueError not raised or incorrect error message"

    @pytest.mark.performance
    def test_find_mod_inverse_large_inputs(self):
        # Arrange
        a, m = 123456789, 987654321  # gcd(123456789, 987654321) = 1
        expected_result = 186471204  # 186471204 is the modular inverse of 123456789 modulo 987654321

        # Act
        result = find_mod_inverse(a, m)

        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"

    @pytest.mark.negative
    def test_find_mod_inverse_negative_inputs(self):
        # Arrange
        a, m = -3, -7  # gcd(-3, -7) = 1
        expected_result = -5  # -5 is the modular inverse of -3 modulo -7

        # Act
        result = find_mod_inverse(a, m)

        # Assert
        assert result == expected_result, f"Expected {expected_result}, but got {result}"
