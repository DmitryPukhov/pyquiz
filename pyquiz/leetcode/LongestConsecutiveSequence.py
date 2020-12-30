from typing import List


class LongestConsecutiveSequence:

    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
        Follow up: Could you implement the O(n) solution?

        Example 1:
        Input: nums = [100,4,200,1,3,2]
        Output: 4
        Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
        Example 2:
        Input: nums = [0,3,7,2,5,8,4,6,0,1]
        Output: 9

        Constraints:
        0 <= nums.length <= 104
        -109 <= nums[i] <= 109
        """
        nset = set(nums)

        best = 0
        for n in nums:
            if n not in nset:
                # Already calculate sequence with n
                continue
            startn = endn = n
            while startn - 1 in nset:
                nset.remove(startn-1)
                startn -= 1
            while endn + 1 in nset:
                nset.remove(endn+1)
                endn += 1
            best = max(best, endn - startn + 1)
        return best
