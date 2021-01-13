from django.test import TestCase

from .models import SequenceSearch

class SequenceSearchTests(TestCase):

    def test_clean_empty_sequence(self):
        """ should raise an exception when clean is called on empty sequence"""
        self.assertRaises(Exception, SequenceSearch.clean, "")

    def test_clean_correct_sequence(self):
        """ should return the same thing for correct sequence """
        self.assertEquals("ACTG", SequenceSearch.clean("ACTG"))

    def test_clean_capitalizes_sequence(self):
        """ should capitalize a sequence"""
        self.assertEquals("ACTG", SequenceSearch.clean("acTG"))

    def test_clean_incorrect_sequence(self):
        """ should throw an exception on an incorrect sequence"""
        self.assertRaises(Exception, SequenceSearch.clean, "ACTX")

    def test_find_match(self):
        """ should throw an exception on an incorrect sequence"""
        match_path = SequenceSearch.findMatches("GGGAGAACCAGGTGGGATTGACAGTGGTAAATGTGTTGACCA").file_path
        self.assertEquals(match_path, "/Users/jonah.spear/Development/ProteinFinder/dnaForm/proteins/NC_000852.faa")
