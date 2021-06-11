import unittest
from typing import List


class Solution:
    """
    Maximum Area of a Piece of Cake After Horizontal and Vertical Cuts
    Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts
    where horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut
    and similarly, verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

    Return the maximum area of a piece of cake after you cut at each horizontal and vertical position
    provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a huge number,
    return this modulo 10^9 + 7.




    Constraints:
    2 <= h, w <= 10^9
    1 <= horizontalCuts.length < min(h, 10^5)
    1 <= verticalCuts.length < min(w, 10^5)
    1 <= horizontalCuts[i] < h
    1 <= verticalCuts[i] < w
    It is guaranteed that all elements in horizontalCuts are distinct.
    It is guaranteed that all elements in verticalCuts are distinct.
    """
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hbounds=[0]+sorted(horizontalCuts) + [h]
        vbounds = [0] + sorted(verticalCuts) + [w]
        hdiff=self.diff(hbounds)
        vdiff = self.diff(vbounds)
        return (max(hdiff)%(1000000000+7))*(max(vdiff)%(1000000000+7))

        return (max(hdiff)%1000000000+7)*(max(vdiff)%1000000000+7)

    def diff(self, lst: List[int]):
        return [lst[i+1]-lst[i] for i in range(len(lst)-1)]

    def maxArea_slow(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:

        # Add bounds
        hbounds = [0] + sorted(horizontalCuts) + [h]
        vbounds = [0] + sorted(verticalCuts) + [w]

        out = 0
        for l in range(len(vbounds)-1):
            for t in range(len(hbounds)-1):
                areaw = vbounds[l + 1] - vbounds[l]
                areah = hbounds[t + 1] - hbounds[t]
                area = areaw * areah
                out = max(out,area)

        return out


class TestMaxArea(unittest.TestCase):

    def test_maxarea_example1(self):
        """
        Example 1:
        Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
        Output: 4
        Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
        """
        self.assertEqual(4, Solution().maxArea(h=5, w=4, horizontalCuts=[1, 2, 4], verticalCuts=[1, 3]))

    def test_maxarea_example2(self):
        """
        Example 2:
        Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
        Output: 6
        Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
        """
        self.assertEqual(6, Solution().maxArea(h=5, w=4, horizontalCuts=[3, 1], verticalCuts=[1]))

    def test_maxarea_example3(self):
        """
        Example 3:
        Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
        Output: 9
        """
        self.assertEqual(9, Solution().maxArea(h=5, w=4, horizontalCuts=[3], verticalCuts=[3]))


if __name__ == '__main__':
    unittest.main()
