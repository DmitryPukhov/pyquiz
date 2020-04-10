# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class MinimumAbsoluteDifferenceInBST:
    """
    Given a binary search tree with non-negative values, find the minimum absolute difference
    between values of any two nodes.
    Example:
    Input:

       1
        \
         3
        /
       2

    Output:
    1

    Explanation:
    The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
    """

    def getMinimumDifference(self, root: TreeNode) -> int:
        # Traverse the tree, get sorted array
        sorted = self.traverse(root)

        # Calc min delta
        d = sorted[len(sorted) - 1] - sorted[0]
        for i in range(1, len(sorted)):
            curd = sorted[i] - sorted[i - 1]
            d = min(d, curd)
        return d

    def traverse(self, root: TreeNode) -> List[int]:
        vals = list()
        if root.left is not None:
            vals.extend(self.traverse(root.left))
        vals.append(root.val)
        if root.right is not None:
            vals.extend(self.traverse(root.right))
        return vals


alg = MinimumAbsoluteDifferenceInBST().getMinimumDifference()
#[1,null,3,2]