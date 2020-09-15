class DecodeWays:
    """
    A message containing letters from A-Z is being encoded to numbers using the following mapping:
    'A' -> 1
    'B' -> 2
    ...
    'Z' -> 26
    Given a non-empty string containing only digits, determine the total number of ways to decode it.

    Example 1:
    Input: "12"
    Output: 2
    Explanation: It could be decoded as "AB" (1 2) or "L" (12).

    Example 2:
    Input: "226"
    Output: 3
    Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
    """
    memo = {}

    def numDecodings(self, s: str) -> int:
        self.memo = {}
        return self.nums(s, 0)

    def nums(self, s: str, i: int) -> int:
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        if i == len(s) - 1:
            return 1
        if i in self.memo: return self.memo[i]
        out = self.nums(s, i + 1) + (self.nums(s, i + 2) if int(s[i:i + 2]) <= 26 else 0)
        self.memo[i] = out
        return out
