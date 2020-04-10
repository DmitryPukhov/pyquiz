from pyquiz.common.ListNode import ListNode


class DoubleLinkedNode(ListNode):
    """
    Linked list node with prev and next ref
    """

    def __init__(self, value, prev=None, next_=None):
        super(DoubleLinkedNode, self).__init__(value, next_)
        self.next_ = next_
        self.prev = prev
