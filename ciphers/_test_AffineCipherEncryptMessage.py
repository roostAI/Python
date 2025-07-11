import pytest
from affine_cipher import encrypt_message, check_keys
import sys
from maths.greatest_common_divisor import gcd_by_iterative

class Test_AffineCipherEncryptMessage:

    SYMBOLS = (
        ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_"abcdefghijklmnopqrstuvwxyz{|}~'
    )

    def test_encrypt_message_valid_key_message(self):
        key = 4545
        message = 'The affine cipher is a type of monoalphabetic substitution cipher.'
        expected_result = 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi'
        assert encrypt_message(key, message) == expected_result

    def test_encrypt_message_invalid_key(self):
        key = -1
        message = 'The affine cipher is a type of monoalphabetic substitution cipher.'
        with pytest.raises(SystemExit) as e:
            encrypt_message(key, message)
        assert str(e.value) == "Key A must be greater than 0 and key B must be between 0 and 94."

    def test_encrypt_message_empty_message(self):
        key = 4545
        message = ''
        assert encrypt_message(key, message) == ''

    def test_encrypt_message_unrecognized_symbols(self):
        key = 4545
        message = 'The affine cipher is a type of monoalphabetic substitution cipher. 123'
        expected_result = 'VL}p MM{I}p~{HL}Gp{vp pFsH}pxMpyxIx JHL O}F{~pvuOvF{FuF{xIp~{HL}Gi 123'
        assert encrypt_message(key, message) == expected_result
