from typing import List


class MaximumSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        nn = len(nums)
        if nn == 0:
            return -2147483648
        elif nn == 1:
            return nums[0]

        sums = [None] * nn
        sums[0] = nums[0]
        maxsum = sums[0]
        for i in range(1,nn):
            sums[i] = max(nums[i] + sums[i-1], nums[i])
            if sums[i] > maxsum:
                maxsum = sums[i]
        return maxsum