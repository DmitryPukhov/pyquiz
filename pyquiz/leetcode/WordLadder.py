import collections
from collections import deque, defaultdict
from typing import List, Set


class WordLadder:
    """
    127. Word Ladder
    Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest
    transformation sequence from beginWord to endWord, such that:

    Only one letter can be changed at a time.
    Each transformed word must exist in the word list.
    Note:

    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.
    You may assume no duplicates in the word list.
    You may assume beginWord and endWord are non-empty and are not the same.

    Example 1:

    Input:
    beginWord = "hit",
    endWord = "cog",
    wordList = ["hot","dot","dog","lot","log","cog"]

    Output: 5

    Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.

    Example 2:

    Input:
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]

    Output: 0

    Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
    """

    def ladderLength(self, beginWord, endWord, wordList):
        """
        For each word create word->transformations and transformation->word dictionaries to not calculate it every cycle
        Then do BFA from beginWord until we transform it to endWord.
        """
        if endWord not in wordList:
            return 0
        # Fill in transformations dictionaries
        wtdict = defaultdict(set)
        twdict = defaultdict(set)

        for w in [beginWord] + wordList:
            for i in range(len(beginWord)):
                trans = w[:i] + '*' + w[i + 1:]
                wtdict[w].add(trans)
                if w != beginWord:
                    twdict[trans].add(w)

        # BFS considering transformation dictionaries
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        while q:
            w, level = q.popleft()
            if w == endWord:
                return level
            if w in visited:
                continue
            for t in wtdict[w]:
                nextwords = twdict[t]
                q.extend([(nw, level+1) for nw in nextwords])
            visited.add(w)
        return 0
