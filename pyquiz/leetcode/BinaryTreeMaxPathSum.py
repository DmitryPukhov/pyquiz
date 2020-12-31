import sys

from pyquiz.common.TreeNode import TreeNode


class BinaryTreeMaxPathSum:
    """
    Binary Tree Maximum Path Sum
    Given a non-empty binary tree, find the maximum path sum.
    For this problem, a path is defined as any node sequence
    from some starting node to any node in the tree along the parent-child connections.
    The path must contain at least one node and does not need to go through the root.

    Example 1:
    Input: root = [1,2,3]
    Output: 6

    Example 2:
    Input: root = [-10,9,20,null,null,15,7]
    Output: 42

    Constraints:
    The number of nodes in the tree is in the range [0, 3 * 104].
    -1000 <= Node.val <= 1000
    """

    def maxPathSum(self, root: TreeNode) -> int:
        if not root:
            # Hard code C INT_MIN to pass leetcode test (~sys.maxsize does not work)
            return -2147483648
        self.out = None
        self.visitNode(root)
        return self.out

    def visitNode(self, node: TreeNode) -> int:
        """
        :param maxsums: map node -> max(node + left branch max, node + right branch max)
        :return maxsum of branch node.left + node.val or node.right + node.val
        """
        if not node:
            return 0
        leftsum = self.visitNode(node.left) if node.left else 0
        rightsum = self.visitNode(node.right) if node.right else 0
        passthroughsum = max([leftsum + node.val + rightsum, leftsum + node.val, rightsum + node.val, node.val])
        self.out = max(self.out, passthroughsum) if self.out is not None else passthroughsum
        return max(node.val,leftsum + node.val, rightsum + node.val)
