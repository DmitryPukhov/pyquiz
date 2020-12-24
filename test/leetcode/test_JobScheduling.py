from unittest import TestCase
from pyquiz.leetcode.JobScheduling import JobScheduling


class TestJobScheduling(TestCase):

    def test_job_scheduling_example1(self):
        """
        Example 1:
        Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
        Output: 120
        Explanation: The subset chosen is the first and fourth job.
        Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
        """
        out = JobScheduling().jobScheduling(startTime=[1, 2, 3, 3], endTime=[3, 4, 5, 6], profit=[50, 10, 40, 70])
        self.assertEqual(120, out)

    def test_job_scheduling_example2(self):
        """
        Example 2:
        Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
        Output: 150
        Explanation: The subset chosen is the first, fourth and fifth job.
        Profit obtained 150 = 20 + 70 + 60.
        """
        out = JobScheduling().jobScheduling(startTime=[1, 2, 3, 4, 6], endTime=[3, 5, 10, 6, 9],
                                            profit=[20, 20, 100, 70, 60])
        self.assertEqual(150, out)

    def test_job_scheduling_example3(self):
        """
        Example 3:
        Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
        Output: 6
        """
        out = JobScheduling().jobScheduling(startTime=[1, 1, 1], endTime=[2, 3, 4], profit=[5, 6, 4])
        self.assertEqual(6, out)

    def test_job_scheduling_singlejob(self):
        out = JobScheduling().jobScheduling(startTime=[1], endTime=[2], profit=[3])
        self.assertEqual(3, out)

    def test_job_scheduling_job1concatjob2(self):
        out = JobScheduling().jobScheduling(startTime=[1,2], endTime=[2,3], profit=[2,3])
        self.assertEqual(5, out)

    def test_job_scheduling_job1gapjob2(self):
        out = JobScheduling().jobScheduling(startTime=[1,3], endTime=[2,4], profit=[2,3])
        self.assertEqual(5, out)

    def test_job_scheduling_job1overlapjob2(self):
        out = JobScheduling().jobScheduling(startTime=[1,2], endTime=[3,4], profit=[4,3])
        self.assertEqual(4, out)

    def test_job_scheduling_job1overlapjob2(self):
        out = JobScheduling().jobScheduling(startTime=[1,2], endTime=[3,4], profit=[4,3])
        self.assertEqual(4, out)
