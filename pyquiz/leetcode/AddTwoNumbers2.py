from pyquiz.common.ListNode import ListNode


class AddTwoNumbers2:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The most significant digit comes first and each of their nodes contain a single digit.
     Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Follow up:
    What if you cannot modify the input lists? In other words, reversing the lists is not allowed.

    Example:
    Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 8 -> 0 -> 7
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Recursive approach
        """

        # Addjust the length with leading zeroes
        l1, l2 = self._adjust_nodes(l1, l2)

        node, hold = self._add_with_hold(l1, l2)
        root = ListNode(1, node) if hold else node
        return root

    def _list_len(self, l: ListNode):
        llen = 0
        node = l
        while node:
            llen += 1
            node = node.next
        return llen

    def _adjust_nodes(self, l1: ListNode, l2: ListNode) -> (ListNode, ListNode):
        """ Add leading zeroes to a smaller list """
        l1len, l2len = self._list_len(l1), self._list_len(l2)
        if l1len == l2len:
            return l1, l2

        zroot = ListNode(0)
        znode = ztail = zroot
        for i in range(0, abs(l1len - l2len)):
            ztail = znode
            znode.next = znode = ListNode(0)

        if l1len < l2len:
            ztail.next, l1 = l1, zroot
        else:
            ztail.next, l2 = l2, zroot
        return l1, l2

    def _add_with_hold(self, l1: ListNode, l2: ListNode):
        """Sum considering hold from recursive rest"""
        if not l1:
            return None, 0
        # Recursively add the rest of the list considering hold
        nextnode, nexthold = self._add_with_hold(l1.next, l2.next)

        summ = (l1.val + l2.val + nexthold)
        node, hold = ListNode(summ % 10, nextnode), summ // 10
        return node, hold
