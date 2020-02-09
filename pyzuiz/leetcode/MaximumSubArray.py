from typing import List


class MaximumSubArray:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        p1 = p2 = 0
        maxs = s = 0
        nn = len(nums)
        while p2 < nn:
            while p2 < nn and s + nums[p2] >= s:
                s += nums[p2]
                p2 += 1
            while p1 <= p2 and s + nums[p1] < s:
                s -= nums[p1]
                p1 += 1
            maxs = max(maxs, s)
            s = 0

        return maxs
