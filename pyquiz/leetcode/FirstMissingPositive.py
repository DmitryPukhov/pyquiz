from typing import List


class Solution:
    """
    Given an unsorted integer array nums, find the smallest missing positive integer.

    Example 1:
    Input: nums = [1,2,0]
    Output: 3

    Example 2:
    Input: nums = [3,4,-1,1]
    Output: 2

    Example 3:
    Input: nums = [7,8,9,11,12]
    Output: 1


    Constraints:
    0 <= nums.length <= 300
    -2^31 <= nums[i] <= 2^31 - 1
    """

    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Algorithm:
        Possible answers are in [1..len(nums)+1]
        Go through nums and rearrange nums.
        If current num is in possible answers interval, put it to n-1 place: nums[num-1]=num if 0 < num < len(nums)
        If current num is out, skip it
        """
        # Possible answers are in [1..len(nums)] or len(nums)+1
        i = 0
        ln = len(nums)

        # Rearrange nums list
        # Go through nums.
        # If current num is in possible answers interval, put it to n-1 place: nums[num-1]=num if 0 < num < len(nums)
        while i < ln:
            n = nums[i]
            if n - 1 == i:
                # num is already in it's place
                i += 1
                continue
            nums[i] = -1
            if n <= 0 or n > ln:
                # n is out
                i += 1
                continue
            # n is in possible interval 1..ln
            while (1 <= n <= ln) and nums[n - 1] != n:
                nums[n - 1], n = n , nums[n - 1]
            i += 1

        # Return first not filled
        for i in range(0, ln):
            n = nums[i]
            if n - 1 != i:
                # Missing value in this place
                return i + 1

        # All nums were filled in => first missing positive is the next after nums
        return ln + 1

        def firstMissingPositive_extramemory(self, nums: List[int]) -> int:
            lennums = len(nums)
            visited = [-1] * lennums
            for i, n in enumerate(nums):
                if not (0 <= n < lennums):
                    continue
                visited[n] = n
            for i, n in enumerate(visited):
                if n != i and i > 0:
                    return i
            return lennums
