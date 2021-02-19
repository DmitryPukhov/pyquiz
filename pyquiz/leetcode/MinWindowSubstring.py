import collections


class Solution:
    """
    Given two strings s and t, return the minimum window in s which will contain all the characters in t.
    If there is no such window in s that covers all characters in t, return the empty string "".
    Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

    Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"
    Output: "BANC"

    Example 2:
    Input: s = "a", t = "a"
    Output: "a"

    Constraints:
    1 <= s.length, t.length <= 105
    s and t consist of English letters.

    Follow up: Could you find an algorithm that runs in O(n) time?
    """

    def minWindow(self, s: str, t: str) -> str:
        tcnt = dict(collections.Counter(t))
        wcnt = collections.defaultdict(int)
        w = ""
        i1 = i2 = 0

        while i2 < len(s):
            # Move i2
            while i2 < len(s):
                c2 = s[i2]
                if c2 in tcnt:
                    # Inc window counter
                    wcnt[c2] += 1
                    # Update window if it contains all the chars from t and smaller
                    d = min([wcnt[c] - tcnt[c] for c in tcnt])
                    if d >= 0:
                        ww = s[i1:i2+1]
                        if not w or len(ww) < len(w): w = ww
                        break
                i2 += 1
            # Move i1
            while i1 <= i2:
                c1 = s[i1]
                # Update window if it contains all the chars from t and smaller
                d = min([wcnt[c] - tcnt[c] for c in tcnt])
                if d >= 0:
                    ww = s[i1:i2+1]
                    if not w or len(ww) < len(w): w = ww
                else:
                    break
                # Move i1
                if c1 in tcnt:
                    wcnt[c1] -= 1
                i1 += 1
            i2+=1
        return w
