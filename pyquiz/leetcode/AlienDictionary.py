import collections
from collections import defaultdict
from typing import List


class AlienDictionary:
    """
    There is a new alien language that uses the English alphabet. However, the order among letters are unknown to you.
    You are given a list of strings words from the dictionary,
    where words are sorted lexicographically by the rules of this new language.
    Derive the order of letters in this language, and return it. If the given input is invalid, return "".
    If there are multiple valid solutions, return any of them.

    Example 1:
    Input: words = ["wrt","wrf","er","ett","rftt"]
    Output: "wertf"

    Example 2:
    Input: words = ["z","x"]
    Output: "zx"

    Example 3:
    Input: words = ["z","x","z"]
    Output: ""
    Explanation: The order is invalid, so return "".

    Constraints:
    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists of only lowercase English letters.
    """

    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        incnt = dict([(c, 0) for w in words for c in w])
        # Fill adjacency list of a graph
        for w1, w2 in zip(words, words[1:]):
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c1 not in adj:
                        adj[c1].add(c2)
                        incnt[c2] += 1
                    break
            else:
                # ???
                if len(w2) < len(w1):
                    return ""

        # BFS
        q = collections.deque([c for c in incnt if incnt[c] == 0])
        out = []
        while q:
            c = q.popleft()
            out.append(c)
            for d in adj[c]:
                incnt[d] -= 1
                if incnt[d] == 0:
                    q.append(d)

        if len(out) < len(incnt):
            # There are cycles
            return ""

        return "".join(out)
