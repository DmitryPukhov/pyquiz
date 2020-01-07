from unittest import TestCase

from pyzuiz.algo.tree.RedBlackTree import RedBlackTree
from pyzuiz.common.RedBlackBinaryTreeNode import RedBlackBinaryTreeNode


class TestRedBlackTree(TestCase):

    def test_insert(self):
        tree = RedBlackTree(None)
        tree.insert(3)
        tree.insert(1)
        tree.insert(5)

        self.assertEqual(3, tree.root.value)
        self.assertEqual(1, tree.root.left.value)
        self.assertEqual(5, tree.root.right.value)

    def test_insert__left(self):
        # Initial tree and the item to insert (+2)
        #    3
        #   / \
        #  1   5
        #   \
        #    +2
        node3 = RedBlackBinaryTreeNode(3)
        node1 = RedBlackBinaryTreeNode(1, node3)
        node3.left = node1
        node5 = RedBlackBinaryTreeNode(5)
        node3.right = node5

        tree = RedBlackTree(node3)

        inserted_node = tree.insert(2)

        self.assertEqual(node1.right, inserted_node)
        self.assertEqual(2, inserted_node.value)

    def test_insert__right(self):
        # Initial tree and the item to insert (+4)
        #    3
        #   / \
        #  1   5
        #     /
        #    +4
        node3 = RedBlackBinaryTreeNode(3)
        node1 = RedBlackBinaryTreeNode(1, node3)
        node3.left = node1
        node5 = RedBlackBinaryTreeNode(5)
        node3.right = node5

        tree = RedBlackTree(node3)

        inserted_node = tree.insert(4)

        self.assertEqual(node5.left, inserted_node)
        self.assertEqual(4, inserted_node.value)
