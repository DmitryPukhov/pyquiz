from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.BinaryTreeRightSideView import BinaryTreeRightSideView


class TestBinaryTreeRightSideView(TestCase):
    def test_right_side_view__example1(self):
        """
        Example:
        Input: [1,2,3,null,5,null,4]
        Output: [1, 3, 4]

        Explanation:

           1            <---
         /   \
        2     3         <---
         \     \
          5     4       <---
        """
        root = TreeNode(1,
                        TreeNode(2,
                                 None,
                                 TreeNode(5)),
                        TreeNode(3,
                                 None,
                                 TreeNode(4)))

        res = BinaryTreeRightSideView().rightSideView(root)
        self.assertEqual([1, 3, 4], res)

    def test_right_side_view__135(self):
        """
           1            <---
         /   \
        2     3         <---
         \
          5            <---
        """
        root = TreeNode(1,
                        TreeNode(2,
                                 None,
                                 TreeNode(5)),
                        TreeNode(3))

        res = BinaryTreeRightSideView().rightSideView(root)
        self.assertEqual([1, 3, 5], res)

    def test_right_side_view__1(self):
        """
           1            <---
         /   \
        2     3         <---
         \
          5            <---
        """
        root = TreeNode(1)

        res = BinaryTreeRightSideView().rightSideView(root)
        self.assertEqual([1], res)

    def test_right_side_view__135neg1(self):
        """
                   1         <---
                 /   \
                2     3      <---
              /  \
            0    5            <---
          /
        -1                    <---
        """
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(0,
                                          TreeNode(-1)),
                                 TreeNode(5)),
                        TreeNode(3))

        res = BinaryTreeRightSideView().rightSideView(root)
        self.assertEqual([1, 3, 5, -1], res)

    def test_right_side_view__allleft(self):
        """
                   1         <---
                 /   \
                2     3      <---
              /  \
            0    5            <---
          /
        -1                    <---
        """
        root = TreeNode(1,
                        None,
                        TreeNode(2,
                                 None,
                                 TreeNode(3)))

        res = BinaryTreeRightSideView().rightSideView(root)
        self.assertEqual([1, 2, 3], res)

    def test_right_side_view__allright(self):
        """
        1         <---
         \
          2      <---
           \
            3      <---
        """
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(3)))

        res = BinaryTreeRightSideView().rightSideView(root)
        self.assertEqual([1, 2, 3], res)

    def test_right_side_view__nodenone(self):
        res = BinaryTreeRightSideView().rightSideView(TreeNode(None))
        self.assertEqual([], res)

    def test_right_side_view__none(self):
        res = BinaryTreeRightSideView().rightSideView(None)
        self.assertEqual([], res)
