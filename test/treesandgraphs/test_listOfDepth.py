from unittest import TestCase

from pyzuiz.common.BinaryTreeNode import BinaryTreeNode
from pyzuiz.treesandgraphs.ListOfDepth import ListOfDepth


class TestListOfDepth(TestCase):
    def test_of(self):
        tree = BinaryTreeNode(1,
                              None,
                              # Left level1
                              BinaryTreeNode(2,
                                             None,
                                             # Level2
                                             BinaryTreeNode(4, None, None, None),
                                             BinaryTreeNode(5, None, None, None)),
                              # Right level1
                              BinaryTreeNode(3,
                                             None,
                                             # Level2
                                             BinaryTreeNode(6, None, None, None),
                                             BinaryTreeNode(7, None, None, None)))

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
                arr.append(node.value)
                node = node.next
            lst.append(arr)
        return lst
