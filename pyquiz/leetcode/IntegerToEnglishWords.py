from unittest import TestCase


class Solution:
    """
    Convert a non-negative integer num to its English words representation.
    Constraints:
    0 <= num <= 231 - 1
    """

    def _buckets_of(self, num: int):
        if num == 0:
            return [0]
        buckets = []
        while num > 0:
            buckets.append(num % 1000)
            num = num // 1000
        buckets.reverse()
        return buckets

    def _words_of(self, num: int):
        """
        Convert num < 1000 to word
        """
        words = []
        digits = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["Zero", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        words_11_19 = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                       "Nineteen"]
        hundred = num // 100
        if hundred > 0:
            words.append(digits[hundred] + " Hundred")
        if 11 <= num % 100 <= 19:
            words.append(words_11_19[num % 100 - 10])
        else:
            ten = (num % 100) // 10
            if ten > 0:
                words.append(tens[ten])
            digit = num % 10
            if digit > 0:
                words.append(digits[digit])
        return " ".join(words)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        dimensionwords = ["", " Thousand", " Million", " Billion"]
        out = []
        buckets = self._buckets_of(num)
        buckets.reverse()
        for i in range(len(buckets))[::-1]:
            n = self._words_of(buckets[i])
            if n:
                w = n + dimensionwords[i]
                out.append(w)
        return " ".join(out)


class TestIntegerToEnglishWords(TestCase):

    def test_buckets_of_123456789(self):
        self.assertEqual([123, 456, 789], Solution()._buckets_of(123456789))

    def test_buckets_of_1(self):
        self.assertEqual([1], Solution()._buckets_of(1))

    def test_buckets_of_0(self):
        self.assertEqual([0], Solution()._buckets_of(0))

    def test_words_of_321(self):
        self.assertEqual("Three Hundred Twenty One", Solution()._words_of(321))


    def test_words_of_1(self):
        self.assertEqual("One", Solution()._words_of(1))

    def test_words_of_10(self):
        self.assertEqual("Ten", Solution()._words_of(10))

    def test_words_of_11(self):
        self.assertEqual("Eleven", Solution()._words_of(11))

    def test_numbertowords_0(self):
        self.assertEqual("Zero", Solution().numberToWords(0))

    def test_numbertowords_example1(self):
        """
        Example 1:
        Input: num = 123
        Output: "One Hundred Twenty Three"
        """
        self.assertEqual("One Hundred Twenty Three", Solution().numberToWords(123))

    def test_numbertowords_example2(self):
        """
        Example 2:
        Input: num = 12345
        Output: "Twelve Thousand Three Hundred Forty Five"
        """
        self.assertEqual("Twelve Thousand Three Hundred Forty Five", Solution().numberToWords(12345))

    def test_numbertowords_example3(self):
        """
        Example 3:
        Input: num = 1234567
        Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
        """
        self.assertEqual("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven",
                         Solution().numberToWords(1234567))

    def test_numbertowords_example4(self):
        """
        Example 4:
        Input: num = 1234567891
        Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
        """
        self.assertEqual(
            "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One",
            Solution().numberToWords(1234567891))
