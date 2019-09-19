from pyzuiz.common.SingleLinkedNode import SingleLinkedNode
from pyzuiz.common.TreeNode import BinaryTreeNode


class ListOfDepth:
    """
    4.3
    List of Depths: Given a binary tree, design an algorithm which creates a linked list of all the nodes
    at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
    """

    def __init__(self):
        # We store heads and tails of linked lists in hash maps
        self._heads = {}
        self._tails = {}

    def of(self, root: BinaryTreeNode):
        # Recursive traverse through the tree and form hash map of levels
        self._traverse(root, 0)

        # Create list of linked lists to return
        lists = []
        for level in self._heads.keys():
            lists.append(self._heads[level])

        return lists

    def _traverse(self, node: BinaryTreeNode, level):
        """
        Traverse node's children adding them to hash map by level
        """
        if node is None:
            return

        if level not in self._heads:
            # First node of this level, create linked list
            self._heads[level] = self._tails[level] = SingleLinkedNode(node.value, None)
        else:
            # Add this node to the tail of this level
            self._tails[level].next = SingleLinkedNode(node.value, None)
            self._tails[level] = self._tails[level].next

        self._traverse(node.left, level + 1)
        self._traverse(node.right, level + 1)
