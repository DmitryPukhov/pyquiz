from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.TrimBST import TrimBST


class TestTrimBST(TestCase):
    def test_trim_bst(self):
        tree = TreeNode(4,
                        TreeNode(2,
                                 TreeNode(1),
                                 TreeNode(3)
                                 ),
                        TreeNode(6,
                                 TreeNode(5),
                                 TreeNode(7)))
        trimmed = TrimBST().trimBST(tree, 3, 5)
        self.assertEqual(trimmed.val, 4)
        self.assertEqual(trimmed.left.val, 3)
        self.assertEqual(trimmed.right.val, 5)

    def test_trim_bst__bad_tree_is_out_of_range(self):
        tree = TreeNode(1,
                        TreeNode(2),
                        TreeNode(3)
                        )
        trimmed = TrimBST().trimBST(tree, 3, 5)
        self.assertEqual(3, trimmed.val)
        self.assertIsNone(trimmed.left)
        self.assertIsNone(trimmed.right)

    def test_trim_bst__bad_tree(self):
        # It is not a BST, but let's it to be trimmed
        tree = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(3),
                                 TreeNode(4)
                                 ),
                        TreeNode(5,
                                 TreeNode(6),
                                 TreeNode(7)
                                 ))
        trimmed = TrimBST().trimBST(tree, 1, 2)
        self.assertEqual(trimmed.val, 1)
        self.assertEqual(trimmed.left.val, 2)
