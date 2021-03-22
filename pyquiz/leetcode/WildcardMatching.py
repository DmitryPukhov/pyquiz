from functools import lru_cache


class Solution:
    """
    Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:
    '?' Matches any single character.
    '*' Matches any sequence of characters (including the empty sequence).
    The matching should cover the entire input string (not partial).

    Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

    Example 2:
    Input: s = "aa", p = "*"
    Output: true
    Explanation: '*' matches any sequence.

    Example 3:
    Input: s = "cb", p = "?a"
    Output: false
    Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

    Example 4:
    Input: s = "adceb", p = "*a*b"
    Output: true
    Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

    Example 5:
    Input: s = "acdcb", p = "a*c?b"
    Output: false

    Constraints:
    0 <= s.length, p.length <= 2000
    s contains only lowercase English letters.
    p contains only lowercase English letters, '?' or '*'.
    """
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dp(s: str, p: str) -> bool:
            # Base case, p is over
            if not p:
                # If p is over
                return not s

            # P still exists, check with different p,s moves
            if p[0] == '?' and s:
                # p is any single character, move both s and p
                return dp(s[1:], p[1:])
            elif p[0] == '*':
                # p is keeny, move s or move p or move both
                return dp(s, p[1:]) or (s and (dp(s[1:], p) or dp(s[1:], p[1:])))
            else:
                # p is just a letter
                return s and s[0] == p[0] and dp(s[1:], p[1:])

        return dp(s, p)
