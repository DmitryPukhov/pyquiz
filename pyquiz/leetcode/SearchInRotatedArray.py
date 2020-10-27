from typing import List


class SearchInRotatedArray:
    """
    You are given an integer array nums sorted in ascending order, and an integer target.
    Suppose that nums is rotated at some pivot unknown to you beforehand
    (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
    If target is found in the array return its index, otherwise, return -1.

    Example 1:
    Input: nums = [4,5,6,7,0,1,2], target = 0
    Output: 4

    Example 2:
    Input: nums = [4,5,6,7,0,1,2], target = 3
    Output: -1

    Example 3:
    Input: nums = [1], target = 0
    Output: -1
    """

    def search(self, nums: List[int], target: int) -> int:
        p = self._search_pivot(nums)
        if nums[len(nums)-1] >=target:
            return self._search_subarray(nums, target, p, len(nums) - 1)
        else:
            return self._search_subarray(nums, target, 0, max(0,p-1))
        return out

    @staticmethod
    def _search_subarray(nums: List[int], target: int, l, r) -> int:
        while l < r:
            p = l + (r - l) // 2
            if nums[p] == target:
                return p
            elif nums[p] > target:
                r = p - 1
            else:
                l = p + 1
        return l if nums[l] == target else -1

    @staticmethod
    def _search_pivot(nums: List[int]):
        l, r = 0, len(nums) - 1
        while l < r:
            p = l + (r - l) // 2
            if nums[l] < nums[r]:
                # Found pivot
                return l
            if nums[p] <= nums[max(l, p - 1)] and nums[p] <= nums[min(r, p + 1)]:
                return p
            # Set new pivot
            if nums[l] > nums[p]:
                r = p - 1
            else:
                l = p + 1
        return l
