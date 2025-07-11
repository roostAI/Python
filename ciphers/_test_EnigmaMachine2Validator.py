from __future__ import annotations
import pytest
from enigma_machine2 import _validator

class Test_EnigmaMachine2Validator:

    @pytest.mark.valid
    def test_validator_with_valid_inputs(self):
        rotor_positions = (1, 1, 1)
        rotor_selection = ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', 'ZJXESIUQLHAVRMDOYGTNFWPBKC')
        plugboard_string = 'POLAND'
        expected_result = ((1, 1, 1), ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', 'ZJXESIUQLHAVRMDOYGTNFWPBKC'), {'P': 'O', 'O': 'P', 'L': 'A', 'A': 'L', 'N': 'D', 'D': 'N'})
        assert _validator(rotor_positions, rotor_selection, plugboard_string) == expected_result

    @pytest.mark.invalid
    def test_validator_with_non_unique_rotor_selection(self):
        rotor_positions = (1, 1, 1)
        rotor_selection = ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'EGZWVONAHDCLFQMSIPJBYUKXTR', 'ZJXESIUQLHAVRMDOYGTNFWPBKC')
        plugboard_string = 'POLAND'
        with pytest.raises(Exception, match="Please use 3 unique rotors"):
            _validator(rotor_positions, rotor_selection, plugboard_string)

    @pytest.mark.negative
    def test_validator_with_out_of_range_rotor_positions(self):
        rotor_positions = (1, 1, 27)
        rotor_selection = ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', 'ZJXESIUQLHAVRMDOYGTNFWPBKC')
        plugboard_string = 'POLAND'
        with pytest.raises(ValueError, match="Third rotor position is not within range of 1..26"):
            _validator(rotor_positions, rotor_selection, plugboard_string)

    @pytest.mark.invalid
    def test_validator_with_invalid_plugboard_string(self):
        rotor_positions = (1, 1, 1)
        rotor_selection = ('EGZWVONAHDCLFQMSIPJBYUKXTR', 'FOBHMDKEXQNRAULPGSJVTYICZW', 'ZJXESIUQLHAVRMDOYGTNFWPBKC')
        plugboard_string = 'POLAN'
        with pytest.raises(Exception, match="Odd number of symbols"):
            _validator(rotor_positions, rotor_selection, plugboard_string)
