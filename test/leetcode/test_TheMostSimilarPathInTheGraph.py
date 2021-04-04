from unittest import TestCase
from pyquiz.leetcode.TheMostSimilarPathInTheGraph import Solution


class TestSolution(TestCase):
    def test_most_similar__example1(self):
        """
        Example 1:
        Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = ["ATL","PEK","LAX","DXB","HND"], targetPath = ["ATL","DXB","HND","LAX"]
        Output: [0,2,4,2]
        Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.
        [0,2,4,2] is equivalent to ["ATL","LAX","HND","LAX"] which has edit distance = 1 with targetPath.
        [0,3,0,2] is equivalent to ["ATL","DXB","ATL","LAX"] which has edit distance = 1 with targetPath.
        [0,3,1,2] is equivalent to ["ATL","DXB","PEK","LAX"] which has edit distance = 1 with targetPath.
        """
        self.assertEqual([0, 2, 4, 2], Solution().mostSimilar(n=5,
                                                              roads=[[0, 2], [0, 3], [1, 2], [1, 3], [1, 4], [2, 4]],
                                                              names=["ATL", "PEK", "LAX", "DXB", "HND"],
                                                              targetPath=["ATL", "DXB", "HND", "LAX"]))

    def test_most_similar__example2(self):
        """
        Example 2:
        Input: n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
        Output: [0,1,0,1,0,1,0,1]
        Explanation: Any path in this graph has edit distance = 8 with targetPath.
        """
        self.assertEqual([0, 1, 0, 1, 0, 1, 0, 1], Solution().mostSimilar(n=4,
                                                                          roads=[[1, 0], [2, 0], [3, 0], [2, 1], [3, 1],
                                                                                 [3, 2]],
                                                                          names=["ATL", "PEK", "LAX", "DXB"],
                                                                          targetPath=["ABC", "DEF", "GHI", "JKL", "MNO",
                                                                                      "PQR", "STU", "VWX"]))

    def test_most_similar__example3(self):
        """
        Example 3:
        Input: n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
        Output: [3,4,5,4,3,2,1]
        Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.
        It's equivalent to ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
        """
        self.assertEqual([3, 4, 5, 4, 3, 2, 1], Solution().mostSimilar(n=6,
                                                                       roads=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]],
                                                                       names=["ATL", "PEK", "LAX", "ATL", "DXB", "HND"],
                                                                       targetPath=["ATL", "DXB", "HND", "DXB", "ATL",
                                                                                   "LAX", "PEK"]))

    def test_most_similar__2cities(self):
        self.assertEqual([0, 1], Solution().mostSimilar(n=2,
                                                        roads=[[0, 1]],
                                                        names=["MSK", "SPB"],
                                                        targetPath=["MSK", "SPB"]))
    def test_most_similar__3cities(self):
        self.assertEqual([0, 2], Solution().mostSimilar(n=3,
                                                        roads=[[0, 1], [0,2]],
                                                        names=["MSK", "SPB", "SYD"],
                                                        targetPath=["SPB", "SYD"]))
