# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from pyquiz.common.ListNode import ListNode


class MergeTwoSortedLists:
    """
    Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
    Example:
    Input: 1->2->4, 1->3->4
    Output: 1->1->2->3->4->4
    """

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n1 = l1
        n2 = l2
        # Result
        l3 = n3 = None

        # Initial step
        if n1 is not None and (n2 is None or n1.val <= n2.val):
            n3 = ListNode(n1.val)
            n1 = n1.next
        elif n2 is not None:
            n3 = ListNode(n2.val)
            n2 = n2.next
        l3 = n3

        # Merge
        while n1 is not None and n2 is not None:
            if n1.val <= n2.val:
                # Add n1, then n2
                n3.next = ListNode(n1.val)
                n1 = n1.next
            else:
                # Add n2, then n1
                n3.next = ListNode(n2.val)
                n2 = n2.next
            # Move forward
            n3 = n3.next

        # rest of n2
        while n2 is not None:
            n3.next = ListNode(n2.val)
            n3 = n3.next
            n2 = n2.next
        # rest of n1
        while n1 is not None:
            n3.next = ListNode(n1.val)
            n3 = n3.next
            n1 = n1.next

        return l3
