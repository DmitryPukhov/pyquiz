from unittest import TestCase
from pyquiz.leetcode.GameOfLife import Solution


class TestSolution(TestCase):

    def test_game_of_life__example1(self):
        """
        Example 1:
        Input: board = [[0,1,0],
                        [0,0,1],
                        [1,1,1],
                        [0,0,0]]
        Output: [[0,0,0],
                 [1,0,1],
                 [0,1,1],
                 [0,1,0]]
        """
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        Solution().gameOfLife(board)
        self.assertEqual([[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]], board)

    def test_game_of_life__example2(self):
        """
        Example 2:
        Input: board = [[1,1],[1,0]]
        Output: [[1,1],[1,1]]
        """
        board = [[1, 1], [1, 0]]
        Solution().gameOfLife(board)
        self.assertEqual([[1, 1], [1, 1]], board)

    def test_game_of_life__1(self):
        board = [[1]]
        Solution().gameOfLife(board)
        self.assertEqual([[0]], board)

    def test_game_of_life__0(self):
        board = [[0]]
        Solution().gameOfLife(board)
        self.assertEqual([[0]], board)
