import unittest

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BinaryTreeLeverOrderTraversal:
    """
    Given the root of a binary tree, return the level order traversal of its nodes' values.
    (i.e., from left to right, level by level).
    """

    def level_order(self, root: TreeNode) -> List[List[int]]:
        out = []
        level = [root] if root else []
        while level:
            next_level = []
            for node in level:
                next_level.extend(filter(None, [node.left, node.right]))
            out.append([node.val for node in level])
            level = next_level
        return out


class BinaryTreeLevelOrderTraversalTest(unittest.TestCase):
    def test_example1(self):
        """
        Example 1:
        Input: root = [3,9,20,null,null,15,7]
        Output: [[3],[9,20],[15,7]]
        """
        head = TreeNode(3,
                        TreeNode(9),
                        TreeNode(20,
                                 TreeNode(15),
                                 TreeNode(7)))
        self.assertEqual([[3], [9, 20], [15, 7]], BinaryTreeLeverOrderTraversal().level_order(head))

    def test_example2(self):
        """
        Example 2:
        Input: root = [1]
        Output: [[1]]
        """
        head = TreeNode(1)
        self.assertEqual([[1]], BinaryTreeLeverOrderTraversal().level_order(head))

    def test_example3(self):
        """
        Example 3:
        Input: root = []
        Output: []
        """
        self.assertEqual([], BinaryTreeLeverOrderTraversal().level_order(None))


if __name__ == '__main__':
    unittest.main()
