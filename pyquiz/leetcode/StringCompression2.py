import collections
from functools import lru_cache


class Solution:
    """
    String Compression II
    Run-length encoding is a string compression method that works by replacing consecutive identical characters
    (repeated 2 or more times) with the concatenation of the character
    and the number marking the count of the characters (length of the run).
    For example, to compress the string "aabccc" we replace "aa" by "a2" and replace "ccc" by "c3".
    Thus the compressed string becomes "a2bc3".
    Notice that in this problem, we are not adding '1' after single characters.

    Given a string s and an integer k. You need to delete at most k characters from s such that the run-length encoded version of s has minimum length.
    Find the minimum length of the run-length encoded version of s after deleting at most k characters.

    Example 1:
    Input: s = "aaabcccd", k = 2
    Output: 4
    Explanation: Compressing s without deleting anything will give us "a3bc3d" of length 6. Deleting any of the characters 'a' or 'c' would at most decrease the length of the compressed string to 5, for instance delete 2 'a' then we will have s = "abcccd" which compressed is abc3d. Therefore, the optimal way is to delete 'b' and 'd', then the compressed version of s will be "a3c3" of length 4.

    Example 2:
    Input: s = "aabbaa", k = 2
    Output: 2
    Explanation: If we delete both 'b' characters, the resulting compressed string would be "a4" of length 2.

    Example 3:
    Input: s = "aaaaaaaaaaa", k = 0
    Output: 3
    Explanation: Since k is zero, we cannot delete anything. The compressed string is "a11" of length 3.


    Constraints:
    1 <= s.length <= 100
    0 <= k <= s.length
    s contains only lowercase English letters.
    """

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:

        @lru_cache(None)
        def f(i, seq_ch, seq_len, k_left):
            if k_left == 0 or i >= len(s):
                return 0

            keep_cost = float('inf')
            del_cost = float('inf')
            if s[i] == seq_ch:
                keep_cost = f(i + 1, seq_ch, seq_len + 1, k_left)
                del_cost = 1+f(i + 1, seq_ch, seq_len+1, k_left - 1)
            else:
                keep_cost = f(i + 1, s[i], 1, k_left)
                del_cost = 1 + f(i + 1, s[i], 1, k_left - 1)
            return min(keep_cost, del_cost)

        return f(0, '', 0, k)


    def getLengthOfOptimalCompression_bad(self, s: str, k: int) -> int:
        # Create sorted counts dictionary
        cnts = []
        cnt = 0
        prevc = s[0]
        for c in s:
            if prevc == c:
                cnt += 1
            else:
                cnts.append(cnt)
                cnt = 1
            prevc = c
        cnts.append(cnt)
        cnts = sorted(cnts, key=lambda n: n % 10)

        # Greedy remove characters
        # cntsnew = []
        while k > 0:
            for i, cnt in enumerate(cnts):
                delta = max(0, (cnt % 10 + 1) if cnt > 10 else cnt)
                k -= delta
                if k < 0:
                    break
                cnt -= delta
                if cnt >= 0:
                    cnts[i] = cnt
            cnts = sorted(cnts, key=lambda n: n % 10)

        # Calculate length
        out = 0
        for cnt in cnts:
            if cnt >= 1:
                out += 1 + len(str(cnt))
            elif cnt == 1:
                out += 1

        return out
