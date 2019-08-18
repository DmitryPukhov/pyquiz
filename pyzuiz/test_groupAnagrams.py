from unittest import TestCase

from pyzuiz.GroupAnagrams import GroupAnagrams


class TestGroupAnagrams(TestCase):

    def test_group_anagrams__normal_case(self):
        res = GroupAnagrams().group_anagrams(['12', '11', '21'])
        self.assertTrue(abs(res.index('12') - res.index('21')) == 1)
        self.assertIn('11', res)

    def test_group_anagrams__no_anagrams(self):
        res = GroupAnagrams().group_anagrams(['1', '2', '3'])
        self.assertIn('1', res)
        self.assertIn('2', res)
        self.assertIn('3', res)
        self.assertEquals(3, len(res))

    def test_group_anagrams__multianagrams(self):
        res = GroupAnagrams().group_anagrams(['12', '12', '21'])
        self.assertEquals(2, res.count('12'))
        self.assertEquals(1, res.count('21'))
