from unittest import TestCase

from pyzuiz.bits.BinaryToString import BinaryToString


class TestBinaryToString(TestCase):

    def setUp(self):
        self.binary_to_string = BinaryToString()

    def test_to_string__good_num_converted(self):
        self.assertEqual('0.1', self.binary_to_string.to_string(0.5))
        self.assertEqual('0.11', self.binary_to_string.to_string(0.75))
        self.assertEqual('0.', self.binary_to_string.to_string(0))
        self.assertEqual('0.', self.binary_to_string.to_string(0))

    def test_to_string__long_num__error(self):
        self.assertEqual('ERROR', self.binary_to_string.to_string(0.111111111111111111111111111111111))
