from unittest import TestCase

from pyquiz.leetcode.TopKFrequent import TopKFrequent


class TestTopKFrequent(TestCase):

    def test_top_kfrequent__example1(self):
        """
        Example 1:
        Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
        Output: ["i", "love"]
        Explanation: "i" and "love" are the two most frequent words.
        Note that "i" comes before "love" due to a lower alphabetical order.        :return:
        """
        self.assertEqual(["i", "love"],
                         TopKFrequent().topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2))

    def test_top_kfrequent__example2(self):
        """
        Example 2:
        Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
        Output: ["the", "is", "sunny", "day"]
        Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
        with the number of occurrence being 4, 3, 2 and 1 respectively.
        """
        self.assertEqual(["the", "is", "sunny", "day"],
                         TopKFrequent().topKFrequent(
                             ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], 4))

    def test_top_kfrequent__alphabetic(self):
        self.assertEqual(["a"],
                         TopKFrequent().topKFrequent(
                             ["a", "b"], 1))

    def test_top_kfrequent__alphabetic2(self):
        words = ["plpaboutit", "jnoqzdute", "sfvkdqf", "mjc", "nkpllqzjzp", "foqqenbey", "ssnanizsav", "nkpllqzjzp",
                 "sfvkdqf", "isnjmy", "pnqsz", "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "cyxwlef", "hhqpvvt", "fvvdtpnzx",
                 "plpaboutit", "sfvkdqf", "mjc", "fvvdtpnzx", "bwumsj", "foqqenbey", "isnjmy", "nkpllqzjzp", "hhqpvvt",
                 "foqqenbey", "fvvdtpnzx", "bwumsj", "hhqpvvt", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute", "foqqenbey",
                 "jnoqzdute", "foqqenbey", "hhqpvvt", "ssnanizsav", "mjc", "foqqenbey", "bwumsj", "ssnanizsav",
                 "fvvdtpnzx", "nkpllqzjzp", "jkqonvenhx", "hhqpvvt", "mjc", "isnjmy", "bwumsj", "pnqsz", "hhqpvvt",
                 "nkpllqzjzp", "jnoqzdute", "pnqsz", "nkpllqzjzp", "jnoqzdute", "foqqenbey", "nkpllqzjzp", "hhqpvvt",
                 "fvvdtpnzx", "plpaboutit", "jnoqzdute", "sfvkdqf", "fvvdtpnzx", "jkqonvenhx", "jnoqzdute",
                 "nkpllqzjzp", "jnoqzdute", "fvvdtpnzx", "jkqonvenhx", "hhqpvvt", "isnjmy", "jkqonvenhx", "ssnanizsav",
                 "jnoqzdute", "jkqonvenhx", "fvvdtpnzx", "hhqpvvt", "bwumsj", "nkpllqzjzp", "bwumsj", "jkqonvenhx",
                 "jnoqzdute", "pnqsz", "foqqenbey", "sfvkdqf", "sfvkdqf"]
        res = TopKFrequent().topKFrequent(words, 1)
        self.assertEqual(["fvvdtpnzx"], res)

    def test_top_kfrequent__alphabetic3(self):
        words = ["nkpllqzjzp", "fvvdtpnzx"]
        res = TopKFrequent().topKFrequent(words, 1)
        self.assertEqual(["fvvdtpnzx"], res)

    def test_top_kfrequent__aaa(self):
        words = ["a", "aa","aaa"]
        res = TopKFrequent().topKFrequent(words, 1)
        self.assertEqual(["a"], res)
