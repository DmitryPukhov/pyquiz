from typing import List


class SubarraySum:
    """
    Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

    Example 1:
    Input:nums = [1,1,1], k = 2
    Output: 2
    """

    def subarraySum(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        summap={0:1}
        sum_=0
        out = 0
        for n in nums:
            sum_+=n
            if sum_-k in summap:
                out += summap[sum_-k]
            summap[sum_]=summap.get(sum_,0)+1
        return out