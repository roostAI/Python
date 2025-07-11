import pytest
import numpy as np
from polybius import PolybiusCipher

class Test_PolybiusCipherEncode:

    @pytest.mark.regression
    def test_encode_lowercase_message(self):
        cipher = PolybiusCipher()
        message = "testmessage"
        encoded_message = cipher.encode(message)
        assert encoded_message == "4415434432154343112215", "The encoded message does not match the expected output."

    @pytest.mark.regression
    def test_encode_uppercase_message(self):
        cipher = PolybiusCipher()
        message = "TestMessage"
        encoded_message = cipher.encode(message)
        assert encoded_message == "4415434432154343112215", "The encoded message does not match the expected output."

    @pytest.mark.regression
    def test_encode_message_with_spaces(self):
        cipher = PolybiusCipher()
        message = "test message"
        encoded_message = cipher.encode(message)
        assert encoded_message == "44154344 32154343112215", "The encoded message does not match the expected output."

    @pytest.mark.regression
    def test_encode_message_with_j(self):
        cipher = PolybiusCipher()
        message = "jtestjmessage"
        encoded_message = cipher.encode(message)
        assert encoded_message == "2415434424154343112215", "The encoded message does not match the expected output."
