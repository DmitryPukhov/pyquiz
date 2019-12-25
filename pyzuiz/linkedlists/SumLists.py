from pyzuiz.common.SingleLinkedNode import SingleLinkedNode


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

    @staticmethod
    def sum(head1: SingleLinkedNode, head2: SingleLinkedNode):
        node1 = head1
        node2 = head2
        # Sum
        head_res = None
        prev_node_res = None
        carry = 0

        while node1 is not None \
                or node2 is not None:
            val1 = node1.value if node1 is not None else 0
            val2 = node2.value if node2 is not None else 0

            s = val1 + val2 + carry
            # Calc carry
            if s >= 10:
                carry = 1
                s %= 10
            else:
                carry = 0

            # Calc sum and add to a new node
            if prev_node_res is not None:
                newnode3 = SingleLinkedNode(s, None)
                prev_node_res.next = newnode3
                prev_node_res = newnode3
            else:
                # Initial step
                prev_node_res = head_res = SingleLinkedNode(s, None)
            node1 = node1.next if node1 is not None else None
            node2 = node2.next if node2 is not None else None

        # Process remained carry if needed
        if carry > 0:
            prev_node_res.next = SingleLinkedNode(carry, None)

        return head_res
