from unittest import TestCase

from pyquiz.leetcode.TaskScheduler import TaskScheduler


class TestTaskScheduler(TestCase):

    def test_least_interval__example1(self):
        """
        Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation:
        A -> B -> idle -> A -> B -> idle -> A -> B
        There is at least 2 units of time between any two same tasks.
        """
        res = TaskScheduler().leastInterval(["A", "A", "A", "B", "B", "B"], 2)
        self.assertEqual(8, res)

    def test_least_interval__example2(self):
        """
        Example 2:
        Input: tasks = ["A","A","A","B","B","B"], n = 0
        Output: 6
        Explanation: On this case any permutation of size 6 would work since n = 0.
        ["A","A","A","B","B","B"]
        ["A","B","A","B","A","B"]
        ["B","B","B","A","A","A"]
        ...
        And so on.
        A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
        """
        res = TaskScheduler().leastInterval(tasks=["A", "A", "A", "B", "B", "B"], n=0)
        self.assertEqual(6, res)

    def test_least_interval__example3(self):
        """
        Example 3:
        Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
        Output: 16
        Explanation:
        One possible solution is
        A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
        """
        res = TaskScheduler().leastInterval(tasks=["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], n=2)
        self.assertEqual(16, res)

    def test_least_interval_aaabbbcccdde(self):
        res = TaskScheduler().leastInterval(["A", "A", "A", "B", "B", "B", "C", "C", "C", "D", "D", "E"], n=2)
        self.assertEqual(12, res)
