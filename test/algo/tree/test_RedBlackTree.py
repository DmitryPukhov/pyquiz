from unittest import TestCase

from pyzuiz.algo.tree.RedBlackTree import RedBlackTree
from pyzuiz.common.RedBlackBinaryTreeNode import RedBlackBinaryTreeNode


class TestRedBlackTree(TestCase):
    def test_get_uncle(self):
        self.fail()

    def test_get_sibling(self):
        self.fail()

    def test_insert(self):
        node3 = RedBlackBinaryTreeNode(3)
        node1 = RedBlackBinaryTreeNode(1, node3)
        node3.right = node1
        node2 = RedBlackBinaryTreeNode(2)
        RedBlackTree().insert(node3, node2)

        self.assertEqual(node2.value, node3.left.value)
        self.assertEqual(node3, node2.parent, node1)
