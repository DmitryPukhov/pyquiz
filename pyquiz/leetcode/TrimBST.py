# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from pyquiz.common.TreeNode import TreeNode


class TrimBST:
    """
    Given a binary search tree and the lowest and highest boundaries as L and R, trim the tree so that all its elements lies in [L, R] (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.

    Example 1:
    Input:
        1
       / \
      0   2

      L = 1
      R = 2

    Output:
        1
          \
           2
    Example 2:
    Input:
        3
       / \
      0   4
       \
        2
       /
      1

      L = 1
      R = 3

    Output:
          3
         /
       2
      /
     1
    """

    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        if root.val < L:
            root = self.trimBST(root.right, L, R)
        elif root.val > R:
            root = self.trimBST(root.left, L, R)
        else:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root
