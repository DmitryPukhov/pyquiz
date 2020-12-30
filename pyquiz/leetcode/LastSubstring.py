from collections import OrderedDict, defaultdict


class LastSubstring:
    """
    Given a string s, return the last substring of s in lexicographical order.

    Example 1:
    Input: "abab"
    Output: "bab"
    Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. The lexicographically maximum substring is "bab".

    Example 2:
    Input: "leetcode"
    Output: "tcode"

    Note:
    1 <= s.length <= 4 * 10^5
    s contains only lowercase English letters.
    """

    def lastSubstring(self, s: str) -> str:
        # 2 pointers technique.
        # Move pointer j until we find s[j:] > s[i:]. If found, set i=j and move j further
        # We need offset trick to not move i if s[i] == s[j], because the answer can start from i
        i, j, offset = 0, 1, 0
        l = len(s)
        while ((i + offset) < l) and ((j + offset) < l):
            if s[i + offset] == s[j + offset]:
                # We cannot move i,j because s[i:] can be an answer
                # So use i+offset, j+offset to compare while chars are equal
                offset += 1
            elif s[i + offset] > s[j + offset]:
                # s[i:] is still candidate to last string
                j += 1
                offset = 0
            else:
                # s[j:] is larger, so move i to j and start from j=i+1
                i = j
                j += 1
                offset = 0
        return s[i:]
