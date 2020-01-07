from graphviz import Graph

from pyzuiz.common.TreeNode import BinaryTreeNode


class TreeRotation:
    """
    Rotate binary tree
    """

    def rotate_left(self, node: BinaryTreeNode, parent: BinaryTreeNode = None):

        if node is None or node.left is None:
            # No node or left child, no rotation
            return node

        tmp_right_left = node.right.left

        # Left -> node
        new_node = node.right
        new_node.left = node
        node.right = tmp_right_left

        return new_node

    def rotate_right(self, node: BinaryTreeNode, parent: BinaryTreeNode = None):

        if node is None or node.left is None:
            # No node or left child, no rotation
            return node

        tmp_left_right = node.left.right

        # Left -> node
        new_node = node.left
        new_node.right = node
        node.left = tmp_left_right

        return new_node

    def visualize(self, node: BinaryTreeNode, g: Graph = None):
        """
        Draw the tree
        """
        is_root = False
        if g is None:
            g = Graph('G', filename='tree_{}.gv'.format(node.value))
            is_root = True
        # Recursive edges of the children
        if node.left is not None:
            g.edge(str(node.value), str(node.left.value))
            self.visualize(node.left, g)
        if node.right is not None:
            g.edge(str(node.value), str(node.right.value))
            self.visualize(node.right, g)

        # Draw the graph
        if is_root:
            g.view()

############# Visualize a sample tree

tr = TreeRotation()

# Original tree
root = BinaryTreeNode(1, BinaryTreeNode(2, BinaryTreeNode(4), BinaryTreeNode(5)), BinaryTreeNode(3))
tr.visualize(root)

# Rotate right
rotated_right = tr.rotate_right(root)
tr.visualize(rotated_right)

# Rotate left
rotated_left = tr.rotate_left(rotated_right)
tr.visualize(rotated_left)
