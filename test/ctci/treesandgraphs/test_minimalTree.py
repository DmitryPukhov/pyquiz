from unittest import TestCase

from pyquiz.ctci.treesandgraphs.MinimalTree import MinimalTree
from pyquiz.common.TreeNode import TreeNode


class TestMinimalTree(TestCase):

    def test_create_bst__single(self):
        bst: TreeNode = MinimalTree().create_bst([1])
        assert bst.val == 1
        assert bst.left is None
        assert bst.right is None

    def test_create_bst__one_child(self):
        bst: TreeNode = MinimalTree().create_bst([1, 2])
        assert bst.val == 2
        assert bst.left.val == 1
        assert bst.right is None

    def test_create_bst__two_children(self):
        bst: TreeNode = MinimalTree().create_bst([1, 2, 3])
        assert bst.val == 2
        assert bst.left.val == 1
        assert bst.right.val == 3
