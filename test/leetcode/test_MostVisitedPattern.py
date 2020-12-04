from unittest import TestCase

from pyquiz.leetcode.MostVisitedPattern import MostVisitedPattern


class TestMostVisitedPattern(TestCase):
    def test_most_visited_pattern(self):
        """
        Example 1:

        Input: username = ["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]
        Output: ["home","about","career"]
        Explanation:
        The tuples in this example are:
        ["joe", 1, "home"]
        ["joe", 2, "about"]
        ["joe", 3, "career"]
        ["james", 4, "home"]
        ["james", 5, "cart"]
        ["james", 6, "maps"]
        ["james", 7, "home"]
        ["mary", 8, "home"]
        ["mary", 9, "about"]
        ["mary", 10, "career"]
        The 3-sequence ("home", "about", "career") was visited at least once by 2 users.
        The 3-sequence ("home", "cart", "maps") was visited at least once by 1 user.
        The 3-sequence ("home", "cart", "home") was visited at least once by 1 user.
        The 3-sequence ("home", "maps", "home") was visited at least once by 1 user.
        The 3-sequence ("cart", "maps", "home") was visited at least once by 1 user.
        """
        username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary"]
        timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        website = ["home", "about", "career", "home", "cart", "maps", "home", "home", "about", "career"]
        res = MostVisitedPattern().mostVisitedPattern(username, timestamp, website)

        self.assertEqual(["home", "about", "career"], res)

    def test_most_visited_pattern__large(self):
        username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary", "mary", "mary",
                    "user", "user", "user", "user", "user", "user", "user", "user", "user", "user", "user", "user",
                    "user", "user", "user", "user", "user", "user", "user", "user", "user", "user", "user", "user",
                    "user", "user", "user", "user", "user", "user", "user", "user", "user", "user", "user", "user",
                    "user", "user"]
        timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
                     28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]
        website = ["home", "cart", "maps", "home", "about", "career", "home", "home", "cart", "maps", "about", "career",
                   "website1", "website2", "website3", "website4", "website5", "website6", "website7", "website8",
                   "website9",
                   "website10", "website11", "website12", "website13", "website14", "website15", "website16",
                   "website17", "website18",
                   "website19", "website20", "website", "website", "website", "website", "website", "website",
                   "website",
                   "website", "website", "website", "website", "website", "website", "website", "website", "website",
                   "website", "website"]
        res = MostVisitedPattern().mostVisitedPattern(username, timestamp, website)

        self.assertEqual(["home", "about", "career"], res)

    def test_most_visited_pattern__key_sort(self):
        username = ["joe", "joe", "joe", "james", "james", "james", "james", "mary", "mary", "mary", "mary", "mary"]
        timestamp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        website = ["home", "cart", "maps", "home", "about", "career", "home", "home", "cart", "maps", "about", "career"]
        res = MostVisitedPattern().mostVisitedPattern(username, timestamp, website)

        self.assertEqual(["home", "about", "career"], res)

    def test_most_visited_pattern__empty(self):
        username = []
        timestamp = []
        website = []
        res = MostVisitedPattern().mostVisitedPattern(username, timestamp, website)
        self.assertEqual([], res)

    def test_most_visited_pattern__single(self):
        username = ["user"]
        timestamp = [1]
        website = ["website"]
        res = MostVisitedPattern().mostVisitedPattern(username, timestamp, website)
        self.assertEqual([], res)

    def test_most_visited_pattern__y_loedo_y(self):
        username = ["dowg", "dowg", "dowg"]
        timestamp = [158931262, 562600350, 148438945]
        website = ["y", "loedo", "y"]
        res = MostVisitedPattern().mostVisitedPattern(username, timestamp, website)
        self.assertEqual(["y", "y", "loedo"], res)
