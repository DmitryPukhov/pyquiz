import heapq
from typing import List


class KthLargestElement:
    """
    Example 1:
    Input: [3,2,1,5,6,4] and k = 2
    Output: 5

    Example 2:
    Input: [3,2,3,1,2,4,5,5,6] and k = 4
    Output: 4

    Note:
    You may assume k is always valid, 1 ≤ k ≤ array's length.
    """
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Quickselect approach
        """
        return self._select(nums, 0, len(nums) - 1, len(nums) - k)

    def _partition(self, nums, left, right, pivot):
        """
        partition nums array around pivot: <less items> pivot <greater items>
        """

        bound = left
        nums[right], nums[pivot] = nums[pivot], nums[right]
        pivot = right
        for i in range(left, right+1):
            if nums[i] < nums[pivot]:
                nums[bound], nums[i] = nums[i], nums[bound]
                bound +=1
        nums[pivot], nums[bound] = nums[bound], nums[pivot]
        pivot = bound

        return pivot

    def _select(self, nums, left, right, ksmallest):
        if left == right:
            return nums[right]
        pivot = self._partition(nums, left, right, left)
        if pivot == ksmallest:
            return nums[pivot]
        elif pivot < ksmallest:
            left = pivot+1
        else:
            right = pivot-1

        return self._select(nums, left, right, ksmallest)

    def findKthLargest_uselib(self, nums: List[int], k: int) -> int:
        return heapq.nlargest(k, nums).pop()

    def findKthLargest_heap(self, nums: List[int], k: int) -> int:
        h = []
        heapq.heapify(h)
        for n in nums:
            heapq.heappush(h, -n)
        out = None
        for i in range(k):
            out = -heapq.heappop(h)
        return out
