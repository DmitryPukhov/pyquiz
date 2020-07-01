from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.TreeTraversalInOrder import TreeTraversalInOrder


class TestTreeTraversalInOrder(TestCase):
    def test_traverse__completed_tree(self):
        # 0.5, 1, 1.5, 2,3
        tree = TreeNode(2,
                        TreeNode(1,  # root-left
                                 TreeNode(0.5),  # root-left-left
                                 TreeNode(1.5)  # root-left-right
                                 ),
                        # Right
                        TreeNode(3))
        original = [0.5, 1, 1.5, 2, 3]
        self.assertListEqual(original, TreeTraversalInOrder.traverse_iterative(tree))
        self.assertListEqual(original, TreeTraversalInOrder().traverse_recursive(tree))

    def test_traverse__single_branch_tree(self):
        # 0.5, 1, 1.5, 2,3
        tree = TreeNode(2,
                        TreeNode(1,  # root-left
                                 TreeNode(0.5),  # root-left-left
                                 TreeNode(1.5)  # root-left-right
                                 ),
                        # Right
                        None)
        original = [0.5, 1, 1.5, 2]
        self.assertListEqual(original, TreeTraversalInOrder.traverse_iterative(tree))
        self.assertListEqual(original, TreeTraversalInOrder().traverse_recursive(tree))

    def test_traverse__empty_tree(self):
        tree = None
        original = []
        self.assertListEqual(original, TreeTraversalInOrder.traverse_iterative(tree))

    def test_traverse__single_node_tree(self):
        tree = TreeNode(1)
        original = [1]
        self.assertListEqual(original, TreeTraversalInOrder.traverse_iterative(tree))
        self.assertListEqual(original, TreeTraversalInOrder().traverse_recursive(tree))
