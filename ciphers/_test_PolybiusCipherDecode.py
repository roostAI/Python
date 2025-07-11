import pytest
import numpy as np
from polybius import PolybiusCipher

class Test_PolybiusCipherDecode:

    def test_decode_valid_message_no_spaces(self):
        cipher = PolybiusCipher()
        encoded_message = "4415434432154343112215"
        expected_decoded_message = "testmessage"
        decoded_message = cipher.decode(encoded_message)
        assert decoded_message == expected_decoded_message, f"Expected {expected_decoded_message}, but got {decoded_message}"

    def test_decode_valid_message_with_spaces(self):
        cipher = PolybiusCipher()
        encoded_message = "44154344 32154343112215"
        expected_decoded_message = "test message"
        decoded_message = cipher.decode(encoded_message)
        assert decoded_message == expected_decoded_message, f"Expected {expected_decoded_message}, but got {decoded_message}"

    def test_decode_invalid_message(self):
        cipher = PolybiusCipher()
        encoded_message = "1234567890"
        with pytest.raises(IndexError):
            cipher.decode(encoded_message)

    def test_decode_empty_message(self):
        cipher = PolybiusCipher()
        encoded_message = ""
        expected_decoded_message = ""
        decoded_message = cipher.decode(encoded_message)
        assert decoded_message == expected_decoded_message, f"Expected {expected_decoded_message}, but got {decoded_message}"
