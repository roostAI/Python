import pytest
from baconian_cipher import encode

class Test_BaconianCipherEncode:
    def test_encode_single_word(self):
        assert encode("hello") == 'AABBBAABAAABABAABABAABBAB'

    def test_encode_sentence(self):
        assert encode("hello world") == 'AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB'

    def test_encode_non_alphabetical(self):
        with pytest.raises(Exception) as e_info:
            encode("hello world!")
        assert str(e_info.value) == "encode() accepts only letters of the alphabet and spaces"

    def test_encode_uppercase(self):
        assert encode("Hello World") == 'AABBBAABAAABABAABABAABBAB BABAAABBABBAAAAABABAAAABB'
