import math

from pyquiz.common.BinaryTreeNode import BinaryTreeNode


class MinimalTree:
    """
    Minimal Tree: Given a sorted (increasing order) array with unique integer elements,
    write an algorithm to create a binary search tree with minimal height.
    Solution: use idea find a median, it is a root node. Repeat recursively for left/right parts
    """

    def create_bst(self, items: []):
        return self.create_bst_part(items, 0, len(items))

    def create_bst_part(self, items: [], start, end):
        # Parent node will be a median of items
        im = math.floor(start + (end - start) / 2)
        node = BinaryTreeNode(items[im], None, None, None)
        # Recursive call to fill left/right children of BST
        if im > start:
            node.left = self.create_bst_part(items, start, im)
        if end > im + 1:
            node.right = self.create_bst_part(items, im, end)
        return node
