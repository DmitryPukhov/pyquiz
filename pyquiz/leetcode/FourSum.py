import unittest
from typing import List


class Solution:
    """
    18. 4Sum
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

    0 <= a, b, c, d < n
    a, b, c, and d are distinct.
    nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.

    Constraints:
    1 <= nums.length <= 200
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    """

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        """
        ksumsdist = set([tuple(sorted(ks)) for ks in self.ksum(4, sorted(nums), target)])
        ksums = sorted([list(ks) for ks in ksumsdist])

        return ksums

    def ksum(self, k: int, nums: List[int], target: int) -> List[List[int]]:
        if k == 2:
            return self.twosum(nums, target)
        out = []
        for i in range(len(nums)):
            ksumprevs = self.ksum(k - 1, nums[i + 1:], target - nums[i])
            ksums = [[nums[i]] + ksumprev for ksumprev in ksumprevs]

            out.extend(ksums)
        return out

    def twosum(self, nums: List[int], target: int) -> List[List[int]]:
        """
        :param nums: sorted list
        :param target: sum
        :return: List of two-elements lists [n1,n2] where n1+n2 = target and n1, n2 in nums
        """
        p1 = 0
        p2 = len(nums) - 1
        out = set()
        while p2 > p1:
            s = nums[p1] + nums[p2]
            if s == target:
                out.add((nums[p1], nums[p2]))
                p1 += 1
            elif s < target:
                p1 += 1
            elif s > target:
                p2 -= 1
        return [[n1, n2] for n1, n2 in out]


class FourSumTestCase(unittest.TestCase):

    def test_fourSum_111111111_4(self):
        self.assertEqual([], sorted(Solution().twosum([1, 1, 1,1,1,1], 4)))

    def test_twoSum_112344_5(self):
        self.assertEqual([[1, 4], [2, 3]], sorted(Solution().twosum([1, 1, 2, 3, 4, 4], 5)))

    def test_twoSum_1234_m1(self):
        self.assertEqual([], sorted(Solution().twosum([1, 2, 3, 4], -1)))

    def test_twoSum_1234m1_15(self):
        self.assertEqual([[1, 4], [2, 3]], sorted(Solution().twosum([1, 2, 3, 4], 5)))

    def test_twoSum_1234_5(self):
        self.assertEqual([[2, 3]], sorted(Solution().twosum([-1, 2, 3, 4], 5)))

    def test_fourSum_1234_20(self):
        self.assertEqual([], Solution().fourSum(nums=[1, 2, 3, 4], target=20))

    def test_fourSum_1234_10(self):
        self.assertEqual([[1,2,3,4]], Solution().fourSum(nums=[1, 2, 3, 4], target=10))

    def test_fourSum_example1(self):
        """
        Example 1:
        Input: nums = [1,0,-1,0,-2,2], target = 0
        Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
        """
        self.assertEqual([[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]],
                         Solution().fourSum(nums=[1, 0, -1, 0, -2, 2], target=0))

    def test_fourSum_example2(self):
        """
        Example 2:
        Input: nums = [2,2,2,2,2], target = 8
        Output: [[2,2,2,2]]
        """
        self.assertEqual([[2, 2, 2, 2]],
                         Solution().fourSum(nums=[2, 2, 2, 2, 2], target=8))


if __name__ == '__main__':
    unittest.main()
