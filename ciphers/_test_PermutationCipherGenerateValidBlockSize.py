import pytest
import random
from permutation_cipher import generate_valid_block_size

class Test_PermutationCipherGenerateValidBlockSize:

    def test_generate_valid_block_size_with_prime_number(self):
        prime_number = 7
        expected_block_size = 1
        actual_block_size = generate_valid_block_size(prime_number)
        assert actual_block_size == expected_block_size, f"Expected block size {expected_block_size}, but got {actual_block_size}"

    def test_generate_valid_block_size_with_power_of_two(self):
        power_of_two = 16
        actual_block_size = generate_valid_block_size(power_of_two)
        assert actual_block_size in [1, 2, 4, 8, 16], f"Expected block size to be a power of 2, but got {actual_block_size}"

    def test_generate_valid_block_size_with_negative_number(self):
        negative_number = -5
        with pytest.raises(ValueError):
            generate_valid_block_size(negative_number)

    def test_generate_valid_block_size_with_zero(self):
        zero = 0
        with pytest.raises(ValueError):
            generate_valid_block_size(zero)
