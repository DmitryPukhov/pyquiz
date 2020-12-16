from typing import List

from pyquiz.common.TreeNode import TreeNode


class ConstructBinaryTreeFromPreorderAndInorder:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Given preorder and inorder traversal of a tree, construct the binary tree.
        Note:
        You may assume that duplicates do not exist in the tree.

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
        if not preorder or not inorder:
            return None
        elif len(preorder) == len(inorder) == 1:
            return TreeNode(preorder[0])

        # Root node val
        val = preorder[0]

        # Calculate left inorder, preorder and node
        leftinorder = inorder[:inorder.index(val)]
        leftpreorder = preorder[1:1 + len(leftinorder)]
        leftnode = self.buildTree(leftpreorder, leftinorder)

        # Calculate right inorder, preorder and node
        rightinorder = inorder[inorder.index(val)+1:]
        rightpreorder = preorder[1 + len(leftinorder):]
        rightnode = self.buildTree(rightpreorder, rightinorder)

        # Build a new node with left and right
        node = TreeNode(preorder[0], leftnode, rightnode)
        return node
