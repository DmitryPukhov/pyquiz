from unittest import TestCase

from pyzuiz.ctci.arraysandstrings.StringCompression import StringCompression


class TestStringCompression(TestCase):

    def test_compress(self):
        compressed = StringCompression().compress("aaabbcc")
        self.assertEqual("a3b2c2", compressed)

        compressed = StringCompression().compress("aaa")
        self.assertEqual("a3", compressed)

        compressed = StringCompression().compress("")
        self.assertEqual("", compressed)

    def test_compress_empty(self):
        compressed = StringCompression().compress("")
        self.assertEqual("", compressed)

    def test_compress_should_return_original(self):
        # If the
        # "compressed" string would not become smaller than the original string, your method should return
        # the original string
        compressed = StringCompression.compress("abc")
        self.assertEqual("abc", compressed)

        compressed = StringCompression.compress("a")
        self.assertEqual("a", compressed)
