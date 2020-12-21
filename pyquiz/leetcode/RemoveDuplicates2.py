from collections import deque
from typing import Deque


class RemoveDuplicates2:
    """
    Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s
    and removing them causing the left and the right side of the deleted substring to concatenate together.
    We repeatedly make k duplicate removals on s until we no longer can.
    Return the final string after all such duplicate removals have been made.
    It is guaranteed that the answer is unique.

    Example 1:
    Input: s = "abcd", k = 2
    Output: "abcd"
    Explanation: There's nothing to delete.

    Example 2:
    Input: s = "deeedbbcccbdaa", k = 3
    Output: "aa"
    Explanation:
    First delete "eee" and "ccc", get "ddbbbdaa"
    Then delete "bbb", get "dddaa"
    Finally delete "ddd", get "aa"

    Example 3:
    Input: s = "pbbcggttciiippooaais", k = 2
    Output: "ps"

    Constraints:
    1 <= s.length <= 10^5
    2 <= k <= 10^4
    s only contains lower case English letters.
    """

    def removeDuplicates(self, s: str, k: int) -> str:
        # Go through s, add tuple (letter, count) to a stack
        stack = []
        for c in s:
            if stack:
                cprev, cnt = stack[-1]
                # Increment or reset count for current letter
                if c == cprev:
                    cnt += 1
                else:
                    cnt = 1
                stack.append((c, cnt))
                # If reached k, clear last duplicates in stack
                if cnt == k:
                    stack = stack[:-k]
            else:
                # Stack was empty if first letter or starting letters were cleared in the stack
                stack.append((c, 1))

        # Stack contains the answer, separate letter from counts and return
        out = ''.join([c for (c, _) in stack])
        return out
