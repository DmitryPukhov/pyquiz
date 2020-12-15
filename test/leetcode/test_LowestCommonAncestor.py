from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.LowestCommonAncestor import LowestCommonAncestor


class TestLowestCommonAncestor(TestCase):

    def test_lowest_common_ancestor_example1(self):
        """
        Example 1:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
        Output: 3
        Explanation: The LCA of nodes 5 and 1 is 3.
        """
        res = LowestCommonAncestor().lowestCommonAncestor(root=TreeNode.of([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
                                                          p=TreeNode(5), q=TreeNode(1))
        self.assertEqual(3, res.val)

    def test_lowest_common_ancestor_example2(self):
        """
        Example 2:
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
        Output: 5
        Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
        """
        res = LowestCommonAncestor().lowestCommonAncestor(root=TreeNode.of([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]),
                                                          p=TreeNode(5), q=TreeNode(4))
        self.assertEqual(5, res.val)

    def test_lowest_common_ancestor_example3(self):
        """
        Example 3:
        Input: root = [1,2], p = 1, q = 2
        Output: 1
        """
        res = LowestCommonAncestor().lowestCommonAncestor(root=TreeNode.of([1, 2]), p=TreeNode(1), q=TreeNode(2))
        self.assertEqual(1, res.val)
