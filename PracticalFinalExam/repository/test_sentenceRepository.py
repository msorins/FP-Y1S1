from unittest import TestCase
from repository.sentenceRepository import *

class TestSentenceRepository(TestCase):
    def test_loadSentence(self):

        sentenceRepositoryObj = SentenceRepository()
        assert len(sentenceRepositoryObj.getState().getSentence()) != 0


    def test_countLetters(self):
        sentenceRepositoryObj = SentenceRepository()

        assert sentenceRepositoryObj.countLetters(['Ana', 'bla']) == 6
        assert sentenceRepositoryObj.countLetters(['bac', 'dac']) == 6
        assert sentenceRepositoryObj.countLetters(['bacalaureat']) == 11
        assert sentenceRepositoryObj.countLetters(['1234', '56', '78' ]) == 8

    def test_scramble(self):
        sentenceRepositoryObj = SentenceRepository()

        assert sentenceRepositoryObj.getState().getSentence() != sentenceRepositoryObj.getState().getSentenceScrambled()

    def test_swap(self):
        sentenceRepositoryObj = SentenceRepository()

        aux = sentenceRepositoryObj.getState().getSentenceScrambled()
        sentenceRepositoryObj.swap(sentenceRepositoryObj.getState().getSentenceScrambled(), 0, 0, 0, 1)
        sentenceRepositoryObj.swap(sentenceRepositoryObj.getState().getSentenceScrambled(), 0, 0, 0, 1)

        assert aux == sentenceRepositoryObj.getState().getSentenceScrambled()
