from unittest import TestCase

from pyquiz.leetcode.WordSearch import WordSearch


class TestWordSearch(TestCase):
    def test_exist__example1(self):
        """
        Example 1:
        Input: board = [["A","B","C","E"],
                        ["S","F","C","S"],
                        ["A","D","E","E"]],
                word = "ABCCED"
        Output: true
        """
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCCED"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__example2(self):
        """
        Example 2:
        Input: board = [["A","B","C","E"],
                        ["S","F","C","S"],
                        ["A","D","E","E"]],
                word = "SEE"
        Output: true
        """
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "SEE"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__example3(self):
        """
        Example 3:
        Input: board = [["A","B","C","E"],
                        ["S","F","C","S"],
                        ["A","D","E","E"]],
                word = "ABCB"
        Output: false
        """
        board = [["A", "B", "C", "E"],
                 ["S", "F", "C", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCB"
        exist = WordSearch().exist(board, word)
        self.assertFalse(exist)

    def test_exist__board_ab_cd_word_a(self):
        board = [["A", "B"],
                 ["C", "D"]]
        word = "A"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_a_word_a(self):
        board = [["A"]]
        word = "A"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_a_word_b(self):
        board = [["A"]]
        word = "B"
        exist = WordSearch().exist(board, word)
        self.assertFalse(exist)

    def test_exist__board_ab_word_b(self):
        board = [["A", "B"]]
        word = "B"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_a_b_word_b(self):
        board = [["A"], ["B"]]
        word = "B"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_ab_cd_word_abdc(self):
        board = [["A", "B"],
                 ["C", "D"]]
        word = "ABDC"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_ab_cd_word_abcda(self):
        board = [["A", "B"],
                 ["C", "D"]]
        word = "ABDCA"
        exist = WordSearch().exist(board, word)
        self.assertFalse(exist)

    def test_exist__board_abce_sfes_adee_word_abceseeefs(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "E", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCESEEEFS"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_abce_sfes_adee_word_abcefsadeese(self):
        board = [["A", "B", "C", "E"],
                 ["S", "F", "E", "S"],
                 ["A", "D", "E", "E"]]
        word = "ABCEFSADEESE"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)

    def test_exist__board_aa_bc_word_abca(self):
        board = [["A", "A"],
                 ["B", "C"]]
        word = "ABCA"
        exist = WordSearch().exist(board, word)
        self.assertTrue(exist)
