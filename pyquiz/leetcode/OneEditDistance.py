class Solution:
    """
   Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.
    A string s is said to be one distance apart from a string t if you can:
    Insert exactly one character into s to get t.
    Delete exactly one character from s to get t.
    Replace exactly one character of s with a different character to get t.

    Example 1:
    Input: s = "ab", t = "acb"
    Output: true
    Explanation: We can insert 'c' into s to get t.

    Example 2:
    Input: s = "", t = ""
    Output: false
    Explanation: We cannot get t from s by only one step.

    Example 3:
    Input: s = "a", t = ""
    Output: true

    Example 4:
    Input: s = "", t = "A"
    Output: true

    Constraints:
    0 <= s.length <= 104
    0 <= t.length <= 104
    s and t consist of lower-case letters, upper-case letters and/or digits.
    """

    def isOneEditDistance(self, s: str, t: str) -> bool:
        sidx=tidx=0
        editdistance=0
        s+="_"
        t+="_"
        # 1 if can insert s , -1 if delete from s, 0 if can replace
        op = 0 if len(s) == len(t) else 1 if len(s) < len(t) else -1

        while sidx < len(s) and tidx < len(t):
            if s[sidx] == t[tidx]:
                sidx +=1
                tidx +=1
                continue
            if editdistance:
                # We already did edit one character
                return False
            # current character differs
            editdistance +=1
            if op == 0:
                # Replace character and move along
                sidx +=1
                tidx +=1
            elif op == 1:
                # Insert into s means moving index of t
                tidx +=1
            elif op == -1:
                # Delete from s means moving index of s
                sidx +=1
        return editdistance == 1


    def isOneEditDistance2(self, s: str, t: str) -> bool:
        lendiff = abs(len(s) - len(t))
        if lendiff > 1:
            return False

        def dp(s, t) -> bool:
            sidx = tidx = 0
            editFlag=False
            while sidx < len(s) and tidx < len(t):
                if s[sidx] != t[tidx]:
                    if editFlag or not (dp(s[sidx + 1:], t[tidx:]) or dp(s[sidx:], t[tidx + 1:]) or dp(s[sidx + 1:], t[tidx + 1:])):
                        return False
                    editFlag = True
                    continue
                sidx+=1
                tidx+=1
            return editFlag

        return dp(s,t)