class TreeNode:
    """
    Binary tree node with left and right child
    """

    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __init__(self, val, parent=None, left=None, right=None):
    #     self.val = val
    #     self.parent = parent
    #     self.left = left
    #     self.right = right

    def __str__(self):
        return str(self.val)
