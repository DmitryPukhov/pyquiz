from collections import defaultdict, deque
from queue import PriorityQueue
from typing import List


class Solution:
    """
    You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
    Return the max sliding window.

    Example 1:
    Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
    Output: [3,3,5,5,6,7]
    Explanation:
    Window position                Max
    ---------------               -----
    [1  3  -1] -3  5  3  6  7       3
     1 [3  -1  -3] 5  3  6  7       3
     1  3 [-1  -3  5] 3  6  7       5
     1  3  -1 [-3  5  3] 6  7       5
     1  3  -1  -3 [5  3  6] 7       6
     1  3  -1  -3  5 [3  6  7]      7

    Example 2:
    Input: nums = [1], k = 1
    Output: [1]

    Example 3:
    Input: nums = [1,-1], k = 1
    Output: [1,-1]

    Example 4:
    Input: nums = [9,11], k = 2
    Output: [11]

    Example 5:
    Input: nums = [4,-2], k = 2
    Output: [4]


    Constraints:
    1 <= nums.length <= 105
    -10^4 <= nums[i] <= 10^4
    1 <= k <= nums.length
    """

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        def clean_q(i: int):
            if q and q[0] == i - k:
                q.popleft()
            while q and nums[i] > nums[q[-1]]:
                q.pop()

        # Indexes of current sliding window max
        q = deque([0])
        out = []

        maxi = 0
        for i, n in enumerate(nums[1:k], 1):
            clean_q(i)
            q.append(i)
            if n > nums[maxi]:
                maxi = i
        out.append(nums[maxi])

        for i, n in enumerate(nums[k:], k):
            clean_q(i)
            q.append(i)
            out.append(nums[q[0]])

        return out

    def maxSlidingWindow_logn(self, nums: List[int], k: int) -> List[int]:
        # Initial heap and counts map, supports repetitive values
        h = PriorityQueue()
        cnt = defaultdict(int)
        for n in nums[:k]:
            cnt[n] += 1
            h.put(-n)

        out = [-h.queue[0]]
        for i in range(0, len(nums) - k):
            # Will start
            n1 = nums[i]
            n2 = nums[i + k]

            # Update cnt and heap
            cnt[n2] += 1
            cnt[n1] -= 1

            h.put(-n2)

            # Find current maximum in the heap
            while h:
                curmax = -h.get()
                if cnt[curmax] > 0:
                    h.put(-curmax)
                    break

            # Current window max, add to out
            out.append(-h.queue[0])

        return out
