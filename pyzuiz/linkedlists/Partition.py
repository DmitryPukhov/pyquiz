from pyzuiz.common.SingleLinkedNode import SingleLinkedNode


class Partition:
    """
    Write code to partition a linked list around a value x, such that all nodes less than x come
    before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
    to be after the elements less than x (see below). The partition element x can appear anywhere in the
    "right partition"; it does not need to appear between the left and right partitions.
    EXAMPLE
    Input: 3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
    Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
    """

    @staticmethod
    def partition(head: SingleLinkedNode, x):
        """
        :param head: linked list head
        :param x: value to partition the list around
        :return: head of partitioned linked list
        """
        head1: SingleLinkedNode = None
        tail1: SingleLinkedNode = None
        head2: SingleLinkedNode = None
        tail2: SingleLinkedNode = None
        cur_node: SingleLinkedNode = head
        while cur_node is not None:
            if cur_node.value >= x:
                # Above x, add to part 2 tail
                if tail2 is not None:
                    # Add current node to part2 tail
                    tail2.next = cur_node
                    tail2 = tail2.next
                else:
                    # If first item in part2, init head2 and tail2
                    head2 = cur_node
                    tail2 = cur_node
            else:
                # Below2 x, add to part 1 tail
                if tail1 is not None:
                    # Add current node to tail1
                    tail1.next = cur_node
                    tail1 = tail1.next
                else:
                    head1 = cur_node
                    tail1 = cur_node

            cur_node = cur_node.next

        # Concat part1 and part 2
        tail1.next = head2

        if head1 is not None:
            return head1
        else:
            return head2
