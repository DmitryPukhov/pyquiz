from unittest import TestCase

from pyquiz.common.ListNode import ListNode
from pyquiz.ctci.linkedlists.Partition import Partition


class TestPartition(TestCase):

    def test_partition__already_partitioned__should_be_untouched(self):
        head = self.as_linked_list([1, 2, 3])
        x = 2
        partitioned = Partition().partition(head, x)

        self.assertListEqual([1, 2, 3], self.as_array(partitioned))

    def test_partition__middle_pivot__should_reverse(self):
        head = self.as_linked_list([3, 2, 1])
        x = 2
        partitioned = Partition().partition(head, x)

        self.assertTrue(self.is_partitioned(partitioned, 1))

    def test_partition__left_pivot__should_partition(self):
        head = self.as_linked_list([3, 2, 1])
        x = 3
        partitioned = Partition().partition(head, x)
        self.assertTrue(self.is_partitioned(partitioned, x))

    @staticmethod
    def is_partitioned(head, x):
        """
        Check whether given linked list partitioned around x.
        :param head: linked list head
        :param x:  pivot
        :return: True if partitioned, false if not
        """
        node = head
        # Are we on the left or on the right partition
        is_left = True
        while node is not None:
            if node.val >= x:
                # We came from left to right partition
                # All next cycles should be on the right
                is_left = False
            elif not is_left and node.val < x:
                # Not partitioned, if we found a value < x on the right
                return False
            node = node.next

        # Nodes were below x on the right and >=x on the left. Partitioned.
        return True

    @staticmethod
    def as_array(node: ListNode):
        """
        Converts linked list to array to use in test assertions
        :param node: linked list head node
        :return: array of linked list values
        """
        arr = []
        while node is not None:
            arr.append(node.val)
            node = node.next
        return arr

    @staticmethod
    def as_linked_list(arr):
        """
        Converts array of values to linked list
        :param arr: array of values
        :return: head node of linked list
        """
        if arr is None or len(arr) == 0:
            return None
        head = None
        last_node = None
        for value in arr:
            node = ListNode(value, None)
            if head is None:
                # First node
                head = node
                last_node = node
            else:
                # Middle or last node
                last_node.next = node
                last_node = node
        return head
