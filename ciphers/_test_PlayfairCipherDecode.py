import pytest
from playfair_cipher import decode

class Test_PlayfairCipherDecode:

    @pytest.mark.regression
    def test_decode_valid_ciphertext_and_key(self):
        ciphertext = "BMZFAZRZDH"
        key = "HAZARD"
        expected_result = "FIREHAZARD"
        assert decode(ciphertext, key) == expected_result

    @pytest.mark.regression
    def test_decode_different_valid_ciphertext_and_key(self):
        ciphertext = "HNBWBPQT"
        key = "AUTOMOBILE"
        expected_result = "DRIVINGX"
        assert decode(ciphertext, key) == expected_result

    @pytest.mark.regression
    def test_decode_rectangle_case(self):
        ciphertext = "SLYSSAQS"
        key = "CASTLE"
        expected_result = "ATXTACKX"
        assert decode(ciphertext, key) == expected_result
