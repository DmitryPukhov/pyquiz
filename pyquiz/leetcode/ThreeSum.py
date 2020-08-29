from typing import List


class ThreeSum:
    """
    Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
    Note:
    The solution set must not contain duplicate triplets.
    Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
      [-1, 0, 1],
      [-1, -1, 2]
    ]
    """

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Algo: for  each a in nums find twoNums b,c: b+c=a
        """
        # Sort first, and one of 3 numbers, say a, should be <=0
        sortednums = sorted(nums)
        out = []
        preva=None
        for ia, a in enumerate(filter(lambda n: n <= 0, sortednums)):
            if a == preva:
                continue
            abc = self.twoSum(ia, sortednums)
            preva=a
            if abc:
                out += abc
        return out

    def twoSum(self, ia: int, sortednums: List[int]) -> List[List[int]]:
        # a<=b<=c, so ia < ib < ic
        out = []
        l, r = ia + 1, len(sortednums) - 1
        lastabc = None
        while l < r:
            if sortednums[l] + sortednums[r] > -sortednums[ia]:
                r -= 1
            elif sortednums[l] + sortednums[r] < -sortednums[ia]:
                l += 1
            else:
                abc = [sortednums[ia], sortednums[l], sortednums[r]]
                if abc != lastabc:
                    out.append(abc)
                    lastabc = abc
                l += 1  # Doesn't matter, could be r-=1
        return out

    def threeSum_bruitforce(self, nums: List[int]) -> List[List[int]]:
        out = set()
        for ia in range(0, len(nums)):
            for ib in range(0, len(nums)):
                for ic in range(0, len(nums)):
                    if ia == ib or ia == ic or ib == ic:
                        continue
                    a, b, c = nums[ia], nums[ib], nums[ic]
                    abc = tuple(sorted((a, b, c)))
                    if a + b + c == 0 and abc not in out:
                        out.add(abc)
        return out
