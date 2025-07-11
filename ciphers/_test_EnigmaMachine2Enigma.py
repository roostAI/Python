from __future__ import annotations
import pytest
from enigma_machine2 import enigma

class Test_EnigmaMachine2Enigma:

    @pytest.mark.regression
    def test_enigma_with_valid_input_and_default_rotor_and_plugboard(self):
        message = "HELLO WORLD"
        rotor_position = (1, 1, 1)
        encrypted_message = enigma(message, rotor_position)
        assert encrypted_message == "FPNCZ QWOBU"
        decrypted_message = enigma(encrypted_message, rotor_position)
        assert decrypted_message == message

    @pytest.mark.regression
    def test_enigma_with_valid_input_and_custom_rotor_and_plugboard(self):
        message = "HELLO WORLD"
        rotor_position = (1, 1, 1)
        rotor_selection = ("EGZWVONAHDCLFQMSIPJBYUKXTR", "FOBHMDKEXQNRAULPGSJVTYICZW", "ZJXESIUQLHAVRMDOYGTNFWPBKC")
        plugboard = "POLAND"
        encrypted_message = enigma(message, rotor_position, rotor_selection, plugboard)
        assert encrypted_message == "FPNCZ QWOBU"
        decrypted_message = enigma(encrypted_message, rotor_position, rotor_selection, plugboard)
        assert decrypted_message == message

    @pytest.mark.negative
    def test_enigma_with_invalid_rotor_position(self):
        message = "HELLO WORLD"
        rotor_position = (0, 1, 1)
        with pytest.raises(ValueError):
            enigma(message, rotor_position)

    @pytest.mark.negative
    def test_enigma_with_invalid_rotor_selection(self):
        message = "HELLO WORLD"
        rotor_position = (1, 1, 1)
        rotor_selection = ("EGZWVONAHDCLFQMSIPJBYUKXTR", "EGZWVONAHDCLFQMSIPJBYUKXTR", "ZJXESIUQLHAVRMDOYGTNFWPBKC")
        with pytest.raises(Exception):
            enigma(message, rotor_position, rotor_selection)

    @pytest.mark.negative
    def test_enigma_with_invalid_plugboard(self):
        message = "HELLO WORLD"
        rotor_position = (1, 1, 1)
        rotor_selection = ("EGZWVONAHDCLFQMSIPJBYUKXTR", "FOBHMDKEXQNRAULPGSJVTYICZW", "ZJXESIUQLHAVRMDOYGTNFWPBKC")
        plugboard = "POLAN"
        with pytest.raises(Exception):
            enigma(message, rotor_position, rotor_selection, plugboard)
