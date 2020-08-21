from unittest import TestCase

from pyquiz.algo.tree.BFSTraversal import BFSTraversal
from pyquiz.common.TreeNode import TreeNode


class TestBFSTraversal(TestCase):
    def test_bfs__some_nodes_empty(self):
        items = BFSTraversal().bfs(TreeNode(1,
                                            TreeNode(2,
                                                     TreeNode(4),
                                                     None
                                                     ),
                                            TreeNode(3,
                                                     None,
                                                     TreeNode(5))))
        self.assertEqual([1, 2, 3, 4, 5], items)

    def test_bfs__empty(self):
        self.assertFalse(BFSTraversal().bfs(None))

    def test_bfs__single(self):
        self.assertEqual([1], BFSTraversal().bfs(TreeNode(1)))
