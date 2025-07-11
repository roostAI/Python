import pytest
from rabin_miller import is_prime_low_num

class Test_RabinMillerIsPrimeLowNum:

    def test_is_prime_low_num_with_low_prime(self):
        assert is_prime_low_num(97) == True, "Test failed! The function should return True for prime numbers in the low_primes list."

    def test_is_prime_low_num_with_high_prime(self):
        assert is_prime_low_num(104729) == True, "Test failed! The function should return True for prime numbers not in the low_primes list."

    def test_is_prime_low_num_with_non_prime(self):
        assert is_prime_low_num(100) == False, "Test failed! The function should return False for non-prime numbers."

    def test_is_prime_low_num_with_negative(self):
        assert is_prime_low_num(-7) == False, "Test failed! The function should return False for negative numbers."
