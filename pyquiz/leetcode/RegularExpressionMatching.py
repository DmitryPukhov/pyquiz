from functools import lru_cache


class Solution:
    """
    Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*' where:
    '.' Matches any single character.​​​​
    '*' Matches zero or more of the preceding element.
    The matching should cover the entire input string (not partial).

    Example 1:
    Input: s = "aa", p = "a"
    Output: false
    Explanation: "a" does not match the entire string "aa".

    Example 2:
    Input: s = "aa", p = "a*"
    Output: true
    Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

    Example 3:
    Input: s = "ab", p = ".*"
    Output: true
    Explanation: ".*" means "zero or more (*) of any character (.)".

    Example 4:
    Input: s = "aab", p = "c*a*b"
    Output: true
    Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

    Example 5:
    Input: s = "mississippi", p = "mis*is*p*."
    Output: false

    Constraints:
    0 <= s.length <= 20
    0 <= p.length <= 30
    s contains only lowercase English letters.
    p contains only lowercase English letters, '.', and '*'.
    It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
    """
    @lru_cache(None)
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if not s:
            if len(p) >= 2 and p[1] == '*':
                # If *, we can move p anyway
                return self.isMatch(s, p[2:])
            else:
                return False

        is_first_match = p[0] == s[0] or p[0] == '.'
        is_keeny_match = len(p) >= 2 and p[1] == '*'
        if is_keeny_match:
            # If wildcard in pattern
            # Move s or pattern to the left and match again a .*
            # is_move_s_match = self.isMatch(s[1:],p) and is_first_match
            # is_move_p_match = self.isMatch(s,p[2:])
            # is_move_both_match = self.isMatch(s[1:],p[2:]) and is_first_match
            # return is_move_s_match or is_move_p_match or is_move_both_match

            # If first matches, we can move s or p or both.
            # If first does not match, we can move p only
            return is_first_match \
                   and (self.isMatch(s[1:], p) \
                        or self.isMatch(s[1:], p[2:])) \
                   or self.isMatch(s, p[2:])

        else:
            # No wildcard in pattern,
            return is_first_match and self.isMatch(s[1:], p[1:])
