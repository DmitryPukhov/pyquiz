class BinaryTreeNode:
    """
    Binary tree node with left and right child
    """

    def __init__(self, value, parent = None, left = None, right = None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.value)
