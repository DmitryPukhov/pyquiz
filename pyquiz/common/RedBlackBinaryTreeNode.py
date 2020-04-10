from enum import Enum
from pyquiz.common.BinaryTreeNode import BinaryTreeNode


class RedBlackBinaryTreeNode(BinaryTreeNode):
    class Color(Enum):
        BLACK = 0
        RED = 1

    def __init__(self, val, parent=None, left=None, right=None):
        super().__init__(val, parent, left, right)
        # New node is red
        self.color: RedBlackBinaryTreeNode.Color = RedBlackBinaryTreeNode.Color.RED
