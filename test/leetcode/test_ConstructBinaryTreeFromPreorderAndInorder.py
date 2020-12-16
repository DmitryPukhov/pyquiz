from unittest import TestCase

from pyquiz.leetcode.ConstructBinaryTreeFromPreorderAndInorder import ConstructBinaryTreeFromPreorderAndInorder


class TestConstructBinaryTreeFromPreorderAndInorder(TestCase):
    def test_build_tree__example1(self):
        """
        For example, given
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        Return the following binary tree:
            3
           / \
          9  20
            /  \
           15   7
        """
        root = ConstructBinaryTreeFromPreorderAndInorder().buildTree(preorder=[3, 9, 20, 15, 7],
                                                                     inorder=[9, 3, 15, 20, 7])
        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(20, root.right.val)
        self.assertEqual(15, root.right.left.val)
        self.assertEqual(7, root.right.right.val)

    def test_build_tree__empty(self):
        root = ConstructBinaryTreeFromPreorderAndInorder().buildTree([], [])
        self.assertIsNone(root)

    def test_build_tree__39120157(self):
        """
        preorder = [3,9,1,20,15,7]
        inorder = [1,9,3,15,20,7]
        Return the following binary tree:
            3
           / \
          9  20
        /    /  \
        1   15   7
        """
        root = ConstructBinaryTreeFromPreorderAndInorder().buildTree(preorder=[3, 9, 1, 20, 15, 7],
                                                                     inorder=[1, 9, 3, 15, 20, 7])
        self.assertEqual(3, root.val)
        self.assertEqual(9, root.left.val)
        self.assertEqual(1, root.left.left.val)
        self.assertEqual(20, root.right.val)
        self.assertEqual(15, root.right.left.val)
        self.assertEqual(7, root.right.right.val)

    def test_build_tree__31_13(self):
        """
        preorder = [3,1]
        inorder = [1,3]
        Return the following binary tree:
            3
           /
          1
        """
        root = ConstructBinaryTreeFromPreorderAndInorder().buildTree(preorder=[3, 1],
                                                                     inorder=[1, 3])
        self.assertEqual(3, root.val)
        self.assertEqual(1, root.left.val)
        self.assertIsNone(root.right)

    def test_build_tree__31_13(self):
        """
        preorder = [3,1]
        inorder = [1,3]
        Return the following binary tree:
            3
           /
          1
        """
        root = ConstructBinaryTreeFromPreorderAndInorder().buildTree(preorder=[3, 1],
                                                                     inorder=[3, 1])
        self.assertEqual(3, root.val)
        self.assertIsNone(root.left)
        self.assertEqual(1, root.right.val)
