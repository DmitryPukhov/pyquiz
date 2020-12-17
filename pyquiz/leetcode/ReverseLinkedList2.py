from pyquiz.common.ListNode import ListNode


class ReverseLinkedList2:
    """
    Reverse Linked List II
    Reverse a linked list from position m to n. Do it in one-pass.
    Note: 1 ≤ m ≤ n ≤ length of list.

    Example:
    Input: 1->2->3->4->5->NULL, m = 2, n = 4
    Output: 1->4->3->2->5->NULL
    """

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        # Find left part tail
        lefttail = head if m > 1 else None
        for i in range(2, m):
            lefttail = lefttail.next
        middletail = lefttail.next if m > 1 else head
        node1 = middletail
        node2 = node1.next
        middletail.next = None
        # Reverse middle part
        for i in range(m, n):
            tmp = node2.next
            node2.next = node1
            node1, node2 = node2, tmp

        # Form linked list from left - middle - right parts
        righthead = node2
        middletail.next = righthead
        middlehead=node1

        if lefttail:
            lefttail.next = middlehead
        else:
            head = middlehead

        return head
