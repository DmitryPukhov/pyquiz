class SingleLinkedNode:
    """
    Single linked list node
    """

    def __init__(self, value, next_):
        self.value = value
        self.next: SingleLinkedNode = next_

    @staticmethod
    def of(values: []):
        """
        Build linked list of values
        """
        head = None
        tail = None
        for v in values:
            node = SingleLinkedNode(v, None)
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
        while node is not None:
            values.append(str(node.value))
            node = node.next

        return ','.join(values)
