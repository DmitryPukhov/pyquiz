import sys
from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.BinaryTreeMaxPathSum import BinaryTreeMaxPathSum


class TestBinaryTreeMaxPathSum(TestCase):
    def test_max_path_sum__example1(self):
        """
        Example 1:
        Input: root = [1,2,3]
        Output: 6
        """
        root = TreeNode.of([1, 2, 3])
        res = BinaryTreeMaxPathSum().maxPathSum(root)
        self.assertEqual(6, res)

    def test_max_path_sum__example2(self):
        """
        Example 2:
        Input: root = [-10,9,20,null,null,15,7]
        Output: 42
        """
        root = TreeNode.of([-10, 9, 20, None, None, 15, 7])
        res = BinaryTreeMaxPathSum().maxPathSum(root)
        self.assertEqual(42, res)

    def test_max_path_sum__single(self):
        res = BinaryTreeMaxPathSum().maxPathSum(TreeNode(1))
        self.assertEqual(1, res)

    def test_max_path_sum__1_2(self):
        res = BinaryTreeMaxPathSum().maxPathSum(TreeNode(1, TreeNode(2)))
        self.assertEqual(3, res)

    def test_max_path_sum__1_null_2(self):
        res = BinaryTreeMaxPathSum().maxPathSum(TreeNode(1, None, TreeNode(2)))
        self.assertEqual(3, res)

    def test_max_path_sum__empty(self):
        res = BinaryTreeMaxPathSum().maxPathSum(None)
        self.assertEqual(-2147483648, res)

    def test_max_1_3_neg10_neg2_none(self):
        res = BinaryTreeMaxPathSum().maxPathSum(TreeNode.of([1, 3, -10, -2, None]))
        self.assertEqual(4, res)

    def test_max_1_neg2_neg3(self):
        res = BinaryTreeMaxPathSum().maxPathSum(TreeNode.of([1, -2, -3]))
        self.assertEqual(1, res)
        #[-1,0,-2,-3]

    def test_sample3(self):
        res = BinaryTreeMaxPathSum().maxPathSum(TreeNode.of([9,6,-3,None,None,-6,2,None,None,2,None,-6,-6,-6]))
        self.assertEqual(16, res)
