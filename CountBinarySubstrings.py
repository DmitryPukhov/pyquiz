from unittest import TestCase


class CountBinarySubstrings:
    """
    Give a binary string s, return the number of non-empty substrings that have the same number of 0's and 1's,
    and all the 0's and all the 1's in these substrings are grouped consecutively.
    Substrings that occur multiple times are counted the number of times they occur.

    Constraints:
    1 <= s.length <= 105
    s[i] is either '0' or '1'.
    """
    def count_binary_substrings(self, s: str) -> int:
        if not s:
            return 0
        counts = []
        cur_cnt = 1
        cur_c = s[0]
        # 0011000111 -> 2233
        for c in s[1:]:
            if c == cur_c:
                cur_cnt += 1
            else:
                counts.append(cur_cnt)
                cur_cnt = 1
                cur_c = c
        counts.append(cur_cnt)
        # Process boundaries
        out = 0
        for i in range(len(counts) - 1):
            out += min(counts[i], counts[i + 1])

        return out


class TestCountBinarySubstrings(TestCase):
    def test_count_binary_substrings_000(self):
        self.assertEqual(0, CountBinarySubstrings().count_binary_substrings(s="000"))

    def test_count_binary_substrings_10(self):
        self.assertEqual(1, CountBinarySubstrings().count_binary_substrings(s="10"))

    def test_count_binary_substrings_01(self):
        self.assertEqual(1, CountBinarySubstrings().count_binary_substrings(s="01"))

    def test_count_binary_substrings_0(self):
        self.assertEqual(0, CountBinarySubstrings().count_binary_substrings(s="0"))

    def test_count_binary_substrings_example1(self):
        """
        Example 1:
        Input: s = "00110011"
        Output: 6
        Explanation: There are 6 substrings that have equal number
        of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
        Notice that some of these substrings repeat and are counted the number of times they occur.
        Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
        """
        self.assertEqual(6, CountBinarySubstrings().count_binary_substrings(s="00110011"))

    def test_count_binary_substrings_example2(self):
        """
        Example 2:
        Input: s = "10101"
        Output: 4
        Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of consecutive 1's and 0's.
        """
        self.assertEqual(4, CountBinarySubstrings().count_binary_substrings(s="10101"))
