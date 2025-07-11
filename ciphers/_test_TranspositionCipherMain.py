import pytest
from transposition_cipher import main, encrypt_message, decrypt_message

class Test_TranspositionCipherMain:

    @pytest.mark.regression
    def test_encrypt_message(self):
        key = 6
        message = 'Harshil Darji'
        expected_output = 'Hlia rDsahrij'
        assert encrypt_message(key, message) == expected_output

    @pytest.mark.regression
    def test_decrypt_message(self):
        key = 6
        message = 'Hlia rDsahrij'
        expected_output = 'Harshil Darji'
        assert decrypt_message(key, message) == expected_output

    @pytest.mark.regression
    def test_main_encrypt(self, monkeypatch):
        inputs = ['Harshil Darji', '6', 'e']
        expected_output = 'Hlia rDsahrij|'
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        assert main() == expected_output

    @pytest.mark.regression
    def test_main_decrypt(self, monkeypatch):
        inputs = ['Hlia rDsahrij', '6', 'd']
        expected_output = 'Harshil Darji|'
        monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
        assert main() == expected_output
