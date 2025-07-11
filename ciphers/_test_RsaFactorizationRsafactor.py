from __future__ import annotations
import math
import random
import pytest
from rsa_factorization import rsafactor

class Test_RsaFactorizationRsafactor:

    def test_known_rsa_factors(self):
        # Test with known RSA factors
        d, e, n = 3, 16971, 25777
        expected_result = [149, 173]
        assert rsafactor(d, e, n) == expected_result

    def test_large_rsa_modulus(self):
        # Test with large RSA modulus
        d, e, n = 7331, 11, 27233
        expected_result = [113, 241]
        assert rsafactor(d, e, n) == expected_result

    def test_prime_rsa_modulus(self):
        # Test with prime RSA modulus
        d, e, n = 4021, 13, 17711
        expected_result = [89, 199]
        assert rsafactor(d, e, n) == expected_result

    def test_non_integer_inputs(self):
        # Test with non-integer inputs
        with pytest.raises(TypeError):
            rsafactor(3.5, 16971, 25777)
        with pytest.raises(TypeError):
            rsafactor(3, 16971.5, 25777)
        with pytest.raises(TypeError):
            rsafactor(3, 16971, 25777.5)
