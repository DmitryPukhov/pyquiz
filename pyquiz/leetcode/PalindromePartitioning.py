from typing import List


class PalindromePartitioning:
    """
    Given a string s, partition s such that every substring of the partition is a palindrome.
    Return all possible palindrome partitioning of s.

    Example:
    Input: "aab"
    Output:
    [
      ["aa","b"],
      ["a","a","b"]
    ]
    """

    def partition(self, s):
        out = []
        pals = set()

        ## Apply dfs
        def dfs(s, i, j, curlist):
            # Left string
            ss = s[i:j] if s else None
            if ss and (ss in pals or ss == ss[::-1]):
                # If left is palindrome, add to current candidate list
                pals.add(ss)
                curlist.append(ss)
                if j == len(s):
                    # Reached the end
                    out.append(curlist)
                    return
            else:
                # Left string is not a palindrome, backtrack
                return

            for jj in range(j, len(s)+1):
                # Dfs in branches after left string
                dfs(s, j, jj, curlist.copy())

        # Apply dfs to all leftmost strings starting from 0 ending to 1..len(s)
        for j in range(1, len(s)+1):
            dfs(s, 0, j, [])
        return out if out else [[]]
