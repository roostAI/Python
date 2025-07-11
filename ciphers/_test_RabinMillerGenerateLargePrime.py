import pytest
import random
from rabin_miller import generate_large_prime

class Test_RabinMillerGenerateLargePrime:

    def test_generate_large_prime(self):
        keysize = 1024
        prime = generate_large_prime(keysize)
        assert prime > 1
        for i in range(2, prime):
            assert (prime % i) != 0, "The number is not prime"
        assert len(bin(prime)[2:]) == keysize, "The length of the prime number is not equal to the keysize"

    @pytest.mark.parametrize("keysize", [512, 1024, 2048])
    def test_generate_large_prime_different_keysizes(self, keysize):
        prime = generate_large_prime(keysize)
        assert prime > 1
        for i in range(2, prime):
            assert (prime % i) != 0, "The number is not prime"
        assert len(bin(prime)[2:]) == keysize, "The length of the prime number is not equal to the keysize"

    def test_generate_large_prime_uniqueness(self):
        keysize = 1024
        primes = [generate_large_prime(keysize) for _ in range(10)]
        assert len(primes) == len(set(primes)), "The prime numbers are not unique"
