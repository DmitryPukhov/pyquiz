from typing import List


class Permutations:
    """
    Given a collection of distinct integers, return all possible permutations.

    Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]
    """

    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        if len(nums) == 1:
            return [nums]
        for i in range(0, len(nums)):
            perms = ([[nums[i]] + right for right in self.permute(nums[:i] + nums[i + 1:])])
            out.extend(perms)
        return out

