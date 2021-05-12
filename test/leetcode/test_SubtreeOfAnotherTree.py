from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.SubtreeOfAnotherTree import SubtreeOfAnotherTree
from pyquiz.leetcode.SubtreeOfAnotherTree import SubtreeOfAnotherTree


class TestSubtreeOfAnotherTree(TestCase):
    def test_is_subtree_example1(self):
        """
        Example 1:
        Input: root = [3,4,5,1,2], subRoot = [4,1,2]
        Output: true
        """
        self.assertTrue(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(3, TreeNode(4, TreeNode(1), TreeNode(2)),
                                                           TreeNode(5)),
                                             subRoot=TreeNode(4, TreeNode(1), TreeNode(2))))

    def test_is_subtree_example2(self):
        """
        Example 2:
        Input: root = [3,4,5,1,2,null,null,0], subRoot = [4,1,2]
        Output: false
        """
        self.assertFalse(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(3,
                                                           TreeNode(4,
                                                                    TreeNode(5),
                                                                    TreeNode(1,
                                                                             TreeNode(0),
                                                                             None)),
                                                           TreeNode(2)),
                                             subRoot=TreeNode(4,
                                                              TreeNode(1),
                                                              TreeNode(2))))

    def test_is_subtree_11(self):
        self.assertTrue(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1),
                                             subRoot=TreeNode(1)))

    def test_is_subtree_112(self):
        self.assertTrue(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1, TreeNode(1), TreeNode(2)),
                                             subRoot=TreeNode(2)))

    def test_is_subtree_1123(self):
        self.assertFalse(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1, TreeNode(1), TreeNode(2)),
                                             subRoot=TreeNode(3)))

    def test_is_subtree_1243_4(self):
        self.assertTrue(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3)),
                                             subRoot=TreeNode(4)))

    def test_is_subtree_123_1234(self):
        self.assertFalse(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1, TreeNode(2, None, TreeNode(3))),subRoot=TreeNode(1, TreeNode(2, None, TreeNode(3, None, TreeNode(5))))))

    def test_is_subtree_11_1(self):
        self.assertTrue(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1, TreeNode(1)), subRoot=TreeNode(1)))

    def test_is_subtree_121_1(self):
        self.assertFalse(
            SubtreeOfAnotherTree().isSubtree(root=TreeNode(1, TreeNode(2, TreeNode(1))), subRoot=TreeNode(2)))
