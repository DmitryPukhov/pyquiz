from typing import List


class WordBreak:
    """
    Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.
    Note:
    The same word in the dictionary may be reused multiple times in the segmentation.
    You may assume the dictionary does not contain duplicate words.

    Example 1:
    Input: s = "leetcode", wordDict = ["leet", "code"]
    Output: true
    Explanation: Return true because "leetcode" can be segmented as "leet code".

    Example 2:
    Input: s = "applepenapple", wordDict = ["apple", "pen"]
    Output: true
    Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
                 Note that you are allowed to reuse a dictionary word.

    Example 3:
    Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
    Output: false
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s or not wordDict:
            return False
        # Recursive with memoization
        memo = dict()
        out = self.find(s, wordDict, 0, memo)
        return out

    def find(self, s: str, wordDict: List[str], start: int, memo: dict) -> bool:
        if start == len(s): return True
        if start in memo: return memo[start]
        # if start in memo and memo[start]: return True
        for end in range(start, len(s) + 1):
            word = s[start:end]
            if word in wordDict:
                if self.find(s, wordDict, end, memo):
                    memo[start] = True
                    return True
        memo[start] = False
        return False
