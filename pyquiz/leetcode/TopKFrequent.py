import collections
from typing import List
import heapq


class TopKFrequent:
    """
    Example 1:
    Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
    Output: ["i", "love"]
    Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.
    Example 2:
    Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
    Output: ["the", "is", "sunny", "day"]
    Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.
    """

    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = [(-freq, word)for (word, freq) in collections.Counter(words).items()]
        heapq.heapify(heap)
        return [word for freq, word in heapq.nsmallest(k,heap)]

