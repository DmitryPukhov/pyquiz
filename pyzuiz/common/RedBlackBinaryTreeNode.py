from enum import Enum
from pyzuiz.common.BinaryTreeNode import BinaryTreeNode


class RedBlackBinaryTreeNode(BinaryTreeNode):

    class Color(Enum):
        BLACK = 0
        RED = 1

    color: Color
