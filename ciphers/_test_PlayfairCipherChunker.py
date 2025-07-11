import pytest
import itertools
from collections.abc import Generator, Iterable
from playfair_cipher import chunker

class Test_PlayfairCipherChunker:

    def test_chunker_normal_sequence(self):
        sequence = "HELLO"
        size = 2
        result = chunker(sequence, size)
        assert isinstance(result, Generator)
        assert list(result) == [('H', 'E'), ('L', 'L'), ('O',)]

    def test_chunker_empty_sequence(self):
        sequence = ""
        size = 2
        result = chunker(sequence, size)
        assert isinstance(result, Generator)
        assert list(result) == []

    def test_chunker_large_size(self):
        sequence = "HELLO"
        size = 10
        result = chunker(sequence, size)
        assert isinstance(result, Generator)
        assert list(result) == [('H', 'E', 'L', 'L', 'O')]

    def test_chunker_zero_size(self):
        sequence = "HELLO"
        size = 0
        result = chunker(sequence, size)
        assert isinstance(result, Generator)
        assert list(result) == []
