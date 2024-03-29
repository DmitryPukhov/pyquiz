from functools import lru_cache


class Solution:
    """
    Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
    You have the following three operations permitted on a word:
    Insert a character
    Delete a character
    Replace a character

    Example 1:
    Input: word1 = "horse", word2 = "ros"
    Output: 3
    Explanation:
    horse -> rorse (replace 'h' with 'r')
    rorse -> rose (remove 'r')
    rose -> ros (remove 'e')

    Example 2:
    Input: word1 = "intention", word2 = "execution"
    Output: 5
    Explanation:
    intention -> inention (remove 't')
    inention -> enention (replace 'i' with 'e')
    enention -> exention (replace 'n' with 'x')
    exention -> exection (replace 'n' with 'c')
    exection -> execution (insert 'u')

    Constraints:

    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
    """

    def minDistance(self, word1: str, word2: str) -> int:
        len1 = len(word1)
        len2 = len(word2)

        @lru_cache(None)
        def dp(i1: int, i2: int) -> int:
            if i1 >= len1 or i2 >= len2:
                return abs(len1-i1-len2+i2)
            out = word1[i1] != word2[i2]
            dist_replace_cont = out + dp(i1 + 1, i2 + 1)
            dist_ins_del1 = 1 + dp(i1 + 1, i2)
            dist_ins_del2 = 1 + dp(i1, i2 + 1)
            return min(dist_replace_cont, dist_ins_del1, dist_ins_del2)

        return dp(0, 0)
