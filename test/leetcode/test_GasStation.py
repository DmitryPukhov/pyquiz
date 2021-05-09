from unittest import TestCase
from pyquiz.leetcode.GasStation import GasStation


class TestGasStation(TestCase):
    def test_can_complete_circuit_example1(self):
        """
        Example 1:
        Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
        Output: 3
        Explanation:
        Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 4. Your tank = 4 - 1 + 5 = 8
        Travel to station 0. Your tank = 8 - 2 + 1 = 7
        Travel to station 1. Your tank = 7 - 3 + 2 = 6
        Travel to station 2. Your tank = 6 - 4 + 3 = 5
        Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
        Therefore, return 3 as the starting index.
        :return:
        """
        self.assertEqual(3, GasStation().canCompleteCircuit(gas=[1, 2, 3, 4, 5], cost=[3, 4, 5, 1, 2]))

    def test_can_complete_circuit_example2(self):
        """
        Example 2:
        Input: gas = [2,3,4], cost = [3,4,3]
        Output: -1
        Explanation:
        You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
        Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
        Travel to station 0. Your tank = 4 - 3 + 2 = 3
        Travel to station 1. Your tank = 3 - 3 + 3 = 3
        You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
        Therefore, you can't travel around the circuit once no matter where you start.
        """
        self.assertEqual(-1, GasStation().canCompleteCircuit(gas=[2, 3, 4], cost=[3, 4, 3]))

    def test_can_complete_circuit_111_121(self):
        self.assertEqual(-1, GasStation().canCompleteCircuit(gas=[1, 1, 1], cost=[1, 2, 1]))

    def test_can_complete_circuit_111_111(self):
        self.assertEqual(0, GasStation().canCompleteCircuit(gas=[1, 1, 1], cost=[1, 1, 1]))

    def test_can_complete_circuit_121_211(self):
        self.assertEqual(1, GasStation().canCompleteCircuit(gas=[1, 2, 1], cost=[2, 1, 1]))

    def test_can_complete_circuit_121_031(self):
        self.assertEqual(0, GasStation().canCompleteCircuit(gas=[1, 2, 1], cost=[0, 3, 1]))

    def test_can_complete_circuit_5828_6566_3(self):
        """
        Input:  [5,8,2,8]
                [6,5,6,6]
        Answer: 3
        """
        self.assertEqual(3, GasStation().canCompleteCircuit(gas=[5, 8, 2, 8], cost=[6, 5, 6, 6]))

    def test_can_complete_circuit_4_5(self):
        self.assertEqual(-1, GasStation().canCompleteCircuit(gas=[4], cost=[5]))

