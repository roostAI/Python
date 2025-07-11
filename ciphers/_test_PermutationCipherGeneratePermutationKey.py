import pytest
import random
from permutation_cipher import generate_permutation_key

class Test_PermutationCipherGeneratePermutationKey:

    def test_generate_permutation_key_with_positive_integer(self):
        random.seed(0)
        block_size = 5
        result = generate_permutation_key(block_size)
        assert len(result) == block_size
        assert sorted(result) == list(range(block_size))

    def test_generate_permutation_key_with_zero(self):
        block_size = 0
        result = generate_permutation_key(block_size)
        assert result == []

    def test_generate_permutation_key_with_negative_integer(self):
        block_size = -5
        with pytest.raises(ValueError):
            generate_permutation_key(block_size)
