import pytest
import sys
from affine_cipher import check_keys
from maths.greatest_common_divisor import gcd_by_iterative

SYMBOLS = (
    ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"abcdefghijklmnopqrstuvwxyz{|}~'
)

class Test_AffineCipherCheckKeys:
    def test_check_keys_encrypt_key_a_one(self):
        with pytest.raises(SystemExit) as e:
            check_keys(1, 5, "encrypt")
        assert str(e.value) == "The affine cipher becomes weak when key A is set to 1. Choose different key"

    def test_check_keys_encrypt_key_b_zero(self):
        with pytest.raises(SystemExit) as e:
            check_keys(5, 0, "encrypt")
        assert str(e.value) == "The affine cipher becomes weak when key B is set to 0. Choose different key"

    def test_check_keys_negative_keys_or_key_b_large(self):
        with pytest.raises(SystemExit) as e:
            check_keys(-5, 5, "encrypt")
        assert str(e.value) == "Key A must be greater than 0 and key B must be between 0 and {len(SYMBOLS) - 1}."

        with pytest.raises(SystemExit) as e:
            check_keys(5, -5, "encrypt")
        assert str(e.value) == "Key A must be greater than 0 and key B must be between 0 and {len(SYMBOLS) - 1}."

        with pytest.raises(SystemExit) as e:
            check_keys(5, len(SYMBOLS), "encrypt")
        assert str(e.value) == "Key A must be greater than 0 and key B must be between 0 and {len(SYMBOLS) - 1}."

    def test_check_keys_not_relatively_prime(self):
        with pytest.raises(SystemExit) as e:
            check_keys(4, 5, "encrypt")
        assert str(e.value) == f"Key A 4 and the symbol set size {len(SYMBOLS)} are not relatively prime. Choose a different key."
