class ListNode:
    """
    Single linked list node
    """

    def __init__(self, value, next_=None):
        self.val = value
        self.next: ListNode = next_

    @staticmethod
    def of(values: []):
        """
        Build linked list of values
        """
        head = None
        tail = None
        for v in values:
            node = ListNode(v, None)
            if tail is not None:
                tail.next = node
                tail = tail.next
            else:
                head = tail = node
        return head

    def str_with_tail(self):
        """
        Build a string with values from linked list. This node is a head
        """
        # Build string with values of linked list
        values = []
        node = self
        max_items = 10
        items = 0
        while node is not None and items < max_items:
            items += 1
            values.append(str(node.val))
            node = node.next

        if items >= max_items:
            values.append('...')

        return ','.join(values)

    def __str__(self):
        return self.str_with_tail()

    def __len__(self):
        length = 1
        node = self
        while node.next is not None:
            length += 1
            node = node.next
        return length
