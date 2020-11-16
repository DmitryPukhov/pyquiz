from typing import List


class MaximumProductSubarray:
    """
    Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

    Example 1:
    Input: [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.

    Example 2:
    Input: [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
    """

    def maxProduct(self, nums: List[int]) -> int:
        """
        The idea came from Kadane's algo https://en.wikipedia.org/wiki/Maximum_subarray_problem
        """
        if not nums:
            return None
        # Track minimum and maximum value between 0, ... 0
        # Because -1 can change min to max
        curmax = curmin = out = nums[0]
        for n in nums[1:]:
            curmax, curmin = (max(n, n * curmax, n * curmin), min(n, n * curmax, n * curmin))
            out = max(curmax, out)

        return out
