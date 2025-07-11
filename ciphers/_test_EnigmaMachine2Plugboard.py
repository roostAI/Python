import pytest
from enigma_machine2 import _plugboard

class Test_EnigmaMachine2Plugboard:

    def test_valid_plugboard_string(self):
        valid_string = 'PICTURES'
        expected_output = {'P': 'I', 'I': 'P', 'C': 'T', 'T': 'C', 'U': 'R', 'R': 'U', 'E': 'S', 'S': 'E'}
        assert _plugboard(valid_string) == expected_output

    def test_odd_length_plugboard_string(self):
        odd_length_string = 'PICTURE'
        with pytest.raises(Exception) as e_info:
            _plugboard(odd_length_string)
        assert str(e_info.value) == 'Odd number of symbols (7)'

    def test_duplicate_characters_plugboard_string(self):
        duplicate_characters_string = 'PICTUREP'
        with pytest.raises(Exception) as e_info:
            _plugboard(duplicate_characters_string)
        assert str(e_info.value) == 'Duplicate symbol (P)'

    def test_empty_plugboard_string(self):
        empty_string = ''
        assert _plugboard(empty_string) == {}
