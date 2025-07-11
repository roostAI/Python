import pytest
from rsa_cipher import get_text_from_blocks

class Test_RsaCipherGetTextFromBlocks:

    @pytest.mark.regression
    def test_get_text_from_blocks_valid_input(self):
        block_ints = [123456, 789012, 345678]
        message_length = 9
        expected_output = "abcdefghi"
        assert get_text_from_blocks(block_ints, message_length) == expected_output

    @pytest.mark.regression
    def test_get_text_from_blocks_empty_blocks(self):
        block_ints = []
        message_length = 5
        expected_output = ""
        assert get_text_from_blocks(block_ints, message_length) == expected_output

    @pytest.mark.regression
    def test_get_text_from_blocks_large_message_length(self):
        block_ints = [123456, 789012, 345678]
        message_length = 15
        expected_output = "abcdefghi"
        assert len(get_text_from_blocks(block_ints, message_length)) == len(expected_output)

    @pytest.mark.regression
    def test_get_text_from_blocks_small_block_size(self):
        block_ints = [123456, 789012, 345678]
        message_length = 9
        block_size = 64
        expected_output = "abcdefghi"
        assert get_text_from_blocks(block_ints, message_length, block_size) == expected_output
