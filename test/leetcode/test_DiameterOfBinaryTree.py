from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.leetcode.DiameterOfBinaryTree import DiameterOfBinaryTree


class TestDiameterOfBinaryTree(TestCase):
    def test_diameter_of_binary_tree_12345(self):
        #[4,-7,-3,null,null,-9,-3,9,-7,-4,null,6,null,-6,-6,null,null,0,6,5,null,9,null,null,-1,-4,null,null,null,-2]
        root = TreeNode(1,
                        TreeNode(2,
                                 TreeNode(4),
                                 TreeNode(5)),
                        TreeNode(3))
        self.assertEqual(3, DiameterOfBinaryTree().diameterOfBinaryTree(root))

    def test_diameter_of_binary_tree_1(self):
        root = TreeNode(1)
        d = DiameterOfBinaryTree().diameterOfBinaryTree(root)
        self.assertEqual(0, d)

    def test_diameter_of_binary_tree_12(self):
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(1, DiameterOfBinaryTree().diameterOfBinaryTree(root))

    def test_diameter_of_binary_tree_123(self):
        root = TreeNode(1, TreeNode(2), TreeNode(3))
        self.assertEqual(2, DiameterOfBinaryTree().diameterOfBinaryTree(root))
