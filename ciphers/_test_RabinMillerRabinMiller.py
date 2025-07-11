import pytest
import random
from rabin_miller import rabin_miller

class Test_RabinMillerRabinMiller:

    @pytest.mark.regression
    def test_rabin_miller_with_prime_number(self):
        assert rabin_miller(7) == True, "Test failed! rabin_miller function could not identify a prime number."

    @pytest.mark.regression
    def test_rabin_miller_with_composite_number(self):
        assert rabin_miller(8) == False, "Test failed! rabin_miller function could not correctly identify a composite number."

    @pytest.mark.performance
    def test_rabin_miller_with_large_prime_number(self):
        assert rabin_miller(104729) == True, "Test failed! rabin_miller function could not handle large prime numbers."

    @pytest.mark.negative
    def test_rabin_miller_with_negative_number(self):
        assert rabin_miller(-7) == False, "Test failed! rabin_miller function could not correctly handle negative numbers."
