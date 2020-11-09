from unittest import TestCase

from pyquiz.leetcode.GroupAnagrams import GroupAnagrams


class TestGroupAnagrams(TestCase):
    def test_group_anagrams_example1(self):
        """
        Example 1:
        Input: strs = ["eat","tea","tan","ate","nat","bat"]
        Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
        """
        # Call
        res = GroupAnagrams().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
        # Assert
        res = sorted([sorted(l) for l in res])
        self.assertEqual([["ate", "eat", "tea"], ["bat"], ["nat", "tan"]], res)

    def test_group_anagrams_example2(self):
        """
        Example 2:
        Input: strs = [""]
        Output: [[""]]
        """
        res = GroupAnagrams().groupAnagrams([""])
        self.assertEqual([[""]], res)

    def test_group_anagrams_example3(self):
        """
        Example 3:
        Input: strs = ["a"]
        Output: [["a"]]
        """
        res = GroupAnagrams().groupAnagrams(["a"])
        self.assertEqual([["a"]], res)
