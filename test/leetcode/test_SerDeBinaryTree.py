from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.SerDeBinaryTree import SerDeBinaryTree


class TestSerDeBinaryTree(TestCase):
    def test_serialize__example1(self):
        """
        Example 1:
           1
         /  \
        2    3
            / \
           4   5
        Input: root = [1,2,3,null,null,4,5]
        Output: [1,2,3,null,null,4,5]
        """
        root = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3,
                                 TreeNode(4),
                                 TreeNode(5)))
        out = SerDeBinaryTree().serialize(root)
        self.assertEqual("1,2,3,null,null,4,5", out)

    def test_deserialize__example1(self):
        """
        Example 1:
           1
         /  \
        2    3
            / \
           4   5
        Input: root = [1,2,3,null,null,4,5]
        Output: [1,2,3,null,null,4,5]
        """
        root = SerDeBinaryTree().deserialize("1,2,3,null,null,4,5")
        self.assertEqual(root.val, 1)
        self.assertEqual(root.left.val, 2)
        self.assertIsNone(root.left.left)
        self.assertIsNone(root.left.right)

        self.assertEqual(root.right.val, 3)
        self.assertEqual(root.right.left.val, 4)
        self.assertIsNone(root.right.left.left)
        self.assertIsNone(root.right.left.right)
        self.assertEqual(root.right.right.val, 5)
        self.assertIsNone(root.right.right.left)
        self.assertIsNone(root.right.right.right)

    def test_serialize_single(self):
        out = SerDeBinaryTree().serialize(TreeNode(1))
        self.assertEqual("1", out)

    def test_serialize_zeroes(self):
        out = SerDeBinaryTree().serialize(TreeNode(0, TreeNode(0), TreeNode(0)))
        self.assertEqual("0,0,0", out)

    def test_deserialize_zero(self):
        root = SerDeBinaryTree().deserialize("0,0,0")
        self.assertEqual(0, root.val)
        self.assertEqual(0, root.left.val)
        self.assertEqual(0, root.right.val)

    def test_deserialize_single(self):
        out = SerDeBinaryTree().deserialize("1")
        self.assertEqual(1, out.val)
        self.assertIsNone(out.left)
        self.assertIsNone(out.right)