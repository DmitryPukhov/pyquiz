# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List

from pyquiz.common.TreeNode import TreeNode


class LowestCommonAncestor:
    """
    Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
    According to the definition of LCA on Wikipedia:
    “The lowest common ancestor is defined between two nodes p and q as the lowest node in T
    that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    Example 1:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
    Output: 3
    Explanation: The LCA of nodes 5 and 1 is 3.

    Example 2:
    Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
    Output: 5
    Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.

    Example 3:
    Input: root = [1,2], p = 1, q = 2
    Output: 1

    Constraints:
    The number of nodes in the tree is in the range [2, 105].
    -109 <= Node.val <= 109
    All Node.val are unique.
    p != q
    p and q will exist in the tree.
    """

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.p_path = self.q_path = None
        # Do dfs and store p and q paths in class variables p_path, q_path
        self.dfs(root, p, q, [])

        # Find LCA in p_path and q_path
        for i in range(0, min(len(self.p_path), len(self.q_path)))[::-1]:
            if self.p_path[i] == self.q_path[i]:
                # Found lowest ancestor
                return self.p_path[i]
        # Went through p and q paths, no common ancestors
        return None

    def dfs(self, node: TreeNode, p: TreeNode, q: TreeNode, path: List[TreeNode]):

        # Found node p, save it's path
        if node.val == p.val:
            self.p_path = path + [node]
        if node.val == q.val:
            self.q_path = path + [node]

        if self.p_path and self.q_path:
            return

        if node.left: self.dfs(node.left, p, q, path + [node])
        if node.right: self.dfs(node.right, p, q, path + [node])
