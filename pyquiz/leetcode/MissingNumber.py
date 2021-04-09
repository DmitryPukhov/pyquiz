from typing import List


class Solution:
    """
    Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
    Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

    Example 1:
    Input: nums = [3,0,1]
    Output: 2
    Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

    Example 2:
    Input: nums = [0,1]
    Output: 2
    Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.

    Example 3:
    Input: nums = [9,6,4,2,3,5,7,0,1]
    Output: 8
    Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.

    Example 4:
    Input: nums = [0]
    Output: 1
    Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.


    Constraints:
    n == nums.length
    1 <= n <= 104
    0 <= nums[i] <= n
    All the numbers of nums are unique.
    """

    def missingNumber(self, nums: List[int]) -> int:
        out = len(nums)
        for i,n in enumerate(nums):
            out ^= n^i
        return out

    def missingNumber_dp(self, nums: List[int]) -> int:

        # Put each number to it's place inside nums
        for i, n in enumerate(nums):
            if (not (0 <= n < len(nums))) or i == n:
                # n is already at it's place or n is out of the range
                i += 1
                continue
            while 0 <= n < len(nums) and nums[n] != n:
                nums[n], n = n, nums[n]
            i += 1

        # Find the first place where n is not found
        for i, n in enumerate(nums):
            if i != n:
                return i

        return len(nums)
