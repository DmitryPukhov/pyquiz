from unittest import TestCase

from pyzuiz.MinimalTree import MinimalTree
from pyzuiz.tools import TreeNode


class TestMinimalTree(TestCase):

    def test_create_bst__single(self):
        bst: TreeNode = MinimalTree().create_bst([1])
        assert bst.value == 1
        assert bst.left is None
        assert bst.right is None

    def test_create_bst__one_child(self):
        bst: TreeNode = MinimalTree().create_bst([1, 2])
        assert bst.value == 2
        assert bst.left.value == 1
        assert bst.right is None

    def test_create_bst__two_children(self):
        bst: TreeNode = MinimalTree().create_bst([1, 2, 3])
        assert bst.value == 2
        assert bst.left.value == 1
        assert bst.right.value == 3
