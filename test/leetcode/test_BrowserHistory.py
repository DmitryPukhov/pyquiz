from unittest import TestCase

from pyquiz.leetcode.BrowserHistory import BrowserHistory


class TestBrowserHistory(TestCase):

    def test_example1(self):
        """
        Example:

        Input:
        ["BrowserHistory","visit","visit","visit","back","back","forward","visit","forward","back","back"]
        [["leetcode.com"],["google.com"],["facebook.com"],["youtube.com"],[1],[1],[1],["linkedin.com"],[2],[2],[7]]
        Output:
        [null,null,null,null,"facebook.com","google.com","facebook.com",null,"linkedin.com","google.com","leetcode.com"]

        Explanation:
        BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
        browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
        browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
        browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
        browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
        browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
        browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
        browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
        browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
        browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
        browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
        """

        bs = BrowserHistory("leetcode.com")
        bs.visit("google.com")
        bs.visit("facebook.com")
        bs.visit("youtube.com")
        self.assertEqual("facebook.com", bs.back(1))
        self.assertEqual("google.com", bs.back(1))
        self.assertEqual("facebook.com", bs.forward(1))
        bs.visit("linkedin.com")

        self.assertEqual("linkedin.com", bs.forward(2))
        self.assertEqual("google.com", bs.back(2))
        self.assertEqual("leetcode.com", bs.back(7))

    def test_visit(self):
        b = BrowserHistory("home")
        self.assertEqual(["home"], b._history)
        self.assertEqual(0, b._pos)

    def test_back(self):
        b = BrowserHistory("home")
        self.assertEqual(["home"], b._history)
        self.assertEqual("home", b.back(1))
        self.assertEqual("home", b.back(2))
        b.visit("page1")
        b.visit("page2")
        b.visit("page3")
        self.assertEqual(3, b._pos)
        self.assertEqual("page2", b.back(1))
        self.assertEqual(2, b._pos)
        self.assertEqual("home", b.back(10))
        self.assertEqual(0, b._pos)
        self.assertEqual(["home", "page1", "page2", "page3"], b._history)

    def test_forward(self):
        b = BrowserHistory("home")
        self.assertEqual("home", b.forward(1))
        self.assertEqual("home", b.forward(2))
