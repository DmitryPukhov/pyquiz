from pyzuiz.tools.SingleLinkedNode import SingleLinkedNode


class DeleteMiddleNode:
    """
    2.3
    Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
    the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
    that node.
    EXAMPLE
    lnput:the node c from the linked lista->b->c->d->e->f
    Result: nothing is returned, but the new linked list looks like a->b->d->e- >f
    """

    @staticmethod
    def delete_middle(middle: SingleLinkedNode):
        """
        Solution: copy data and next ref from next node to given.
        It does not work for the last node
        """
        next_node = middle.next_
        middle.next_ = next_node.next_
        middle.value = next_node.value
