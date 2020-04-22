from unittest import TestCase

from pyquiz.common.TreeNode import TreeNode
from pyquiz.ctci.treesandgraphs.ListOfDepth import ListOfDepth


class TestListOfDepth(TestCase):
    def test_of(self):
        tree = TreeNode(1,
                        None,
                        # Left level1
                        TreeNode(2,
                                 None,
                                 # Level2
                                 TreeNode(4, None, None, None),
                                 TreeNode(5, None, None, None)),
                        # Right level1
                        TreeNode(3,
                                 None,
                                 # Level2
                                 TreeNode(6, None, None, None),
                                 TreeNode(7, None, None, None)))

        # Get linked lists of depths according to quiz requirements
        res = ListOfDepth().of(tree)

        # Translate linked lists to list
        lst = self.as_list(res)

        self.assertListEqual(lst[0], [1])
        self.assertListEqual(lst[1], [2, 3])
        self.assertListEqual(lst[2], [4, 5, 6, 7])

    @staticmethod
    def as_list(heads):
        """
        Converts list of linked lists to list of arrays.
        This needed for comparison in tests
        """
        lst = []
        for head in heads:
            node = head
            arr = []
            while node is not None:
                arr.append(node.val)
                node = node.next
            lst.append(arr)
        return lst
