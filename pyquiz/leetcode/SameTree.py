# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from pyquiz.common.TreeNode import TreeNode


class Solution:
    """
     Given two binary trees, write a function to check if they are the same or not.
    Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

    Example 1:
    Input:     1         1
              / \       / \
             2   3     2   3

            [1,2,3],   [1,2,3]
    Output: true

    Example 2:
    Input:     1         1
              /           \
             2             2

            [1,2],     [1,null,2]
    Output: false

    Example 3:
    Input:     1         1
              / \       / \
             2   1     1   2

            [1,2,1],   [1,1,2]
    Output: false
    """

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is q:
            return True
        return p is not None and q is not None \
               and p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
