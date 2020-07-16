from enum import Enum
from pyquiz.common.TreeNode import TreeNode


class RedBlackTreeNode(TreeNode):
    class Color(Enum):
        BLACK = 0
        RED = 1

    def __init__(self, val, parent=None, left=None, right=None):
        self.parent = parent
        super().__init__(val, left, right)
        # New node is red
        self.color: RedBlackTreeNode.Color = RedBlackTreeNode.Color.RED
