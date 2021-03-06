from typing import Optional

from pyquiz.common.RedBlackBinaryTreeNode import RedBlackTreeNode


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

    def __init__(self, root: RedBlackTreeNode):
        self.root = root

    def insert(self, value):
        """
        Insert a value, then recolor or rebalance the tree
        """
        node = RedBlackTreeNode(value)
        # Standard BST insertion
        if self.root is None:
            # Insert the root to empty tree
            self.root = node
            self.root.color = RedBlackTreeNode.Color.BLACK
        else:
            # Normal insertion
            node = self._insert_node(self.root, RedBlackTreeNode(value))
            node.color = RedBlackTreeNode.Color.RED

        # Do rebalancing
        self._rebalance(node)
        return node

    def _insert_node(self, root: RedBlackTreeNode, node: RedBlackTreeNode):
        if root.val > node.val:
            if root.left is not None:
                # Go left
                self._insert_node(root.left, node)
            else:
                # Add left leaf
                root.left = node
                node.parent = root
        else:
            if root.right is not None:
                # Go right
                self._insert_node(root.right, node)
            else:
                # Add right leaf
                root.right = node
                node.parent = root
        return node

    def _rebalance(self, node: RedBlackTreeNode):
        """
        3) Do following if color of x’s parent is not BLACK and x is not root.
        a) If x’s uncle is RED (Grand parent must have been black from property 4)
        (i) Change color of parent and uncle as BLACK.
        (ii) color of grand parent as RED.
        (iii) Change x = x’s grandparent, repeat steps 2 and 3 for new x.
        redBlackCase2

        b) If x’s uncle is BLACK, then there can be four configurations for x, x’s parent (p) and x’s grandparent (g) (This is similar to AVL Tree)
        i) Left Left Case (p is left child of g and x is left child of p)
        ii) Left Right Case (p is left child of g and x is right child of p)
        iii) Right Right Case (Mirror of case i)
        iv) Right Left Case (Mirror of case ii)

        Following are operations to be performed in four subcases when uncle is BLACK.
        """
        if node == self.root:
            node.color = RedBlackTreeNode.Color.BLACK
            return

        if node == self.root or node.parent.color == RedBlackTreeNode.Color.BLACK or node is None or node.parent.parent is None:
            # Our new node is red, parent is black - nothing to rebalance
            return

        # If node and node's parent are red, do rebalancing
        uncle = self._get_uncle(node)
        if uncle is None:
            return

        if uncle.color == RedBlackTreeNode.Color.RED:
            # If uncle is red (grand parent and nephews must be black)
            node.parent.color = uncle.color = RedBlackTreeNode.Color.BLACK
            node.parent.parent.color = RedBlackTreeNode.Color.RED
            self._rebalance(node.parent.parent)
        # If uncle is black, for cases
        elif node.parent.left == node and node.parent.parent.left == node.parent:
            # left left case
            self._rebalance_left_left(node)
        elif node.parent.right == node and node.parent.parent.right == node.parent:
            # right right case
            self._rebalance_left_left(node)
        elif node.parent.left == node and node.parent.parent.right == node.parent:
            # left right case
            self._rebalance_left_right(node)
        elif node.parent.right == node and node.parent.parent.left == node.parent:
            # right left case
            self._rebalance_right_left(node)

    @staticmethod
    def _rebalance_left_left(x):
        """
        Right rotate g and swap colors of g and p
                g                        p
             /     \                  /     \
         p(red)     u     --->   x(red)    g(red)
         /           \                       \
      x(red)                                  u
        """
        p = x.parent
        g = p.parent
        u = g.right
        # Rotate right
        p.parent = g.parent
        g.parent = p
        g.left = p.right
        (p.color, g.color) = (g.color, p.color)

    @staticmethod
    def _rebalance_left_right(x):
        """
        left rotate  p, right rotate g and swap colors of g and x
                g                        g                       x
             /     \                  /     \                 /     \
         p(red)     u     --->   x(red)     u    -->     p(red)     g(red)
         \           \            /                                   \
         x(red)                p(red)                                 u
        """
        p = x.parent
        g = p.parent
        u = g.right
        # left rotate p
        x.parent = p.parent
        p.parent = x
        x.left = p
        p.right = x.left
        # right rotate g and swap colors of g and x
        x.parent = g.parent
        g.parent = x
        g.left = x.right
        x.right = g
        (g.color, x.color) = (x.color, g.color)

    @staticmethod
    def _rebalance_right_right(x):
        """
        Left rotate g and swap colors of g and p
                g                        p
             /     \                  /    \
           u     p(red)     --->   g(red)   x
                     \             /
                    x(red)        u
        """
        p = x.parent
        g = p.parent
        u = g.left
        # Rotate right
        p.parent = g.parent
        g.parent = p
        g.right = p.left
        (p.color, g.color) = (g.color, p.color)

    @staticmethod
    def _rebalance_right_left(x):
        """
        Right rotate  p, left  rotate g and swap colors of g and x
                g                       g                       x
             /    \                  /    \                 /     \
            u     p(red)--->        u     x(red)   -->   g(red)    p(red)
                 /                         \            /
             x(red)                        p(red)      u
        """
        p = x.parent
        g = p.parent
        u = g.right
        # Right rotate p
        x.parent = p.parent
        p.parent = x
        x.right = p
        p.left = x.right
        # right rotate g and swap colors of g and x
        x.parent = g.parent
        g.parent = x
        g.right = x.left
        x.left = g
        (g.color, x.color) = (x.color, g.color)

    @staticmethod
    def _get_uncle(node: RedBlackTreeNode):
        if node.parent is None or node.parent.parent is None:
            return None
        grandparent: RedBlackTreeNode = node.parent.parent
        uncle: RedBlackTreeNode = grandparent.left if grandparent.right == node.parent else grandparent.right
        return uncle
