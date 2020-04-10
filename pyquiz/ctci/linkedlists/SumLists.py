from pyquiz.common.ListNode import ListNode


class SumLists:
    """
    2.5 You have two numbers, represented by a
    a linked list, where each node contains a single
    digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
    function that adds the two numbers and returns the sum as a linked list.
    Sum Lists: You have two numbers represented by
    EXAMPLE
    Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
    Output: 2 -> 1 -> 9. That is, 912.
    FOLLOW UP
    Suppose the digits are stored in forward order. Repeat the above problem.
    EXAMPLE
    lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
    Output: 9 -> 1 -> 2. That is, 912.
    Hints: #7, #30, #71, #95, #109
    """

    def sum(self, head1: ListNode, head2: ListNode):
        """
        Sum of two numbers, represented by linked lists in direct order
        Idea: alight the lists, go from left to right, store sum from 0 to 18 without carry, sum list is reversed
        Then go through sum list from right to left, calculating sum from 0 to 9 using carry, reversing the list
        As a result we have sum list from left to right
        """
        head1, head2 = self._align(head1, head2)
        node1, node2 = head1, head2
        head_res = node_sum = node_sum_left = None

        # Calc reversed sum list, numbers from 0 to 18 without carry
        while node1 is not None and node2 is not None:
            node_sum = ListNode(node1.val + node2.val, node_sum_left)
            # First step
            if head_res is None:
                head_res = node_sum
            # Step right
            node_sum_left = node_sum
            node1 = node1.next
            node2 = node2.next

        # Apply carry, reverse sum list
        carry:int = 0
        node_sum_left = node_sum.next
        node_sum.next = None
        while node_sum_left is not None:
            # Apply carry
            carry = (node_sum.val + carry) // 10
            node_sum.val = (node_sum.val + carry) % 10
            # Reverse the node
            new_left = node_sum_left.next
            node_sum_left.next = node_sum
            node_sum = node_sum_left
            node_sum_left = new_left

        # If carry, add new head
        node_sum.val += carry
        carry = node_sum.val // 10
        node_sum.val %= 10
        if carry > 0:
            head_res = ListNode(1, node_sum)

        return head_res

    @staticmethod
    def _align(head1: ListNode, head2: ListNode):
        """
        Left pad smaller linked lists with zeroes to make sizes equal
        :return: aligned_head1, aligned_head2
        """
        node1 = head1
        node2 = head2
        # Go to the tail of list1 or list2
        while node1.next is not None and node2.next is not None:
            node1 = node1.next
            node2 = node2.next

        if node1.next is None and node2.next is None:
            # If lists are of equal size, no align
            return head1, head2

        # Go to the tail of longer list and calculate delta size
        (longer_head, longer_node) = (head1, node1) if node1.next is not None else (head2, node2)
        pad_head = None
        pad_node = None
        while longer_node.next is not None:
            if pad_head is None:
                # First
                pad_head = pad_node = ListNode(0, None)
            else:
                # Add next node to pad list
                pad_node.next = ListNode(0, None)
                pad_node = pad_node.next
            longer_node = longer_node.next

        # Insert paddings  before the head of shorter list
        pad_node.next = head2 if longer_head == head1 else head1

        return (pad_head, head2) if longer_head == head2 else (head1, pad_head)

    @staticmethod
    def sum_of_reversed(head1: ListNode, head2: ListNode):
        """
        Sum of two numbers, represented by linked lists in reverse order
        """
        node1 = head1
        node2 = head2
        # Sum
        head_res = None
        prev_node_res = None
        carry = 0

        while node1 is not None \
                or node2 is not None:
            val1 = node1.val if node1 is not None else 0
            val2 = node2.val if node2 is not None else 0

            s = val1 + val2 + carry
            # Calc carry
            if s >= 10:
                carry = 1
                s %= 10
            else:
                carry = 0

            # Calc sum and add to a new node
            if prev_node_res is not None:
                newnode3 = ListNode(s, None)
                prev_node_res.next = newnode3
                prev_node_res = newnode3
            else:
                # Initial step
                prev_node_res = head_res = ListNode(s, None)
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None

        # Process remained carry if needed
        if carry > 0:
            prev_node_res.next = ListNode(carry, None)

        return head_res
