from pyzuiz.common.RedBlackBinaryTreeNode import RedBlackBinaryTreeNode


class RedBlackTree:
    """
    Implementation of red-black self-balancing binary tree
    https://en.wikipedia.org/wiki/Red–black_tree

    In addition to the requirements imposed on a binary search tree the following must be satisfied by a red–black tree:[16]

    Each node is either red or black.
    The root is black. This rule is sometimes omitted. Since the root can always be changed from red to black, but not necessarily vice versa, this rule has little effect on analysis.
    All leaves (NIL) are black.
    If a node is red, then both its children are black.
    Every path from a given node to any of its descendant NIL nodes contains the same number of black nodes.
    """
    root: RedBlackBinaryTreeNode = None

    def getUncle(self, node: RedBlackBinaryTreeNode):
        if node is None:
            return None
        self.getSibling(self.getParent(node))

    def getSibling(self, node: RedBlackBinaryTreeNode):
        if node is None:
            return None

    def insert(self, root: RedBlackBinaryTreeNode, node: RedBlackBinaryTreeNode):

        if root.value > node.value:
            if root.left is not None:
                # Go left
                self.insert(root.left, node.value)
            else:
                #
                root.left = node
        else:
            if root.right is not None:
                # Go right
                self.insert(root.right, node.value)
            else:
                root.right = node
        node.color = RedBlackBinaryTreeNode.Color.RED
        node.parent = root

