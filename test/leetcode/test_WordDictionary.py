from unittest import TestCase

from pyquiz.leetcode.WordDictionary import WordDictionary


class TestWordDictionary(TestCase):
    def test_example1(self):
        """
          Input
        ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
        [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
        Output
        [null,null,null,null,false,true,true,true]
        """
        wd = WordDictionary()
        wd.addWord("bad")
        wd.addWord("dad")
        self.assertFalse(wd.search("pad"))
        self.assertTrue(wd.search(".ad"))
        self.assertTrue(wd.search("b.."))

    def test_example2(self):
        """
        ["WordDictionary","addWord","addWord","addWord","addWord","search","search","addWord","search","search","search","search","search","search"]
        [[],["at"],["and"],["an"],["add"],["a"],[".at"],["bat"],[".at"],["an."],["a.d."],["b."],["a.d"],["."]]
        Output
        [null,null,null,null,null,true,false,null,true,true,false,true,true,true]
        Expected
        [null,null,null,null,null,false,false,null,true,true,false,false,true,false]
        """
        wd = WordDictionary()
        wd.addWord("at")
        wd.addWord("and")
        wd.addWord("an")
        wd.addWord("add")
        self.assertFalse(wd.search("a"))
        self.assertFalse(wd.search(".ad"))
        wd.addWord("bat")
        self.assertTrue(wd.search(".at"))
        self.assertTrue(wd.search("an."))

        self.assertFalse(wd.search("a.d."))
        self.assertFalse(wd.search("b."))
        self.assertTrue(wd.search("a.d"))
        self.assertFalse(wd.search("."))
