class BinaryHeap:
    """
    Max binary heap implementation
    """

    def __init__(self):
        # 1 - based array
        self._arr = [0]

    def insert(self, value):
        self._arr.append(value)
        self._arr[0] += 1
        self.heapify_up(self._arr[0])

    def heapify_up(self, i):
        """
        Bubble i'th element up
        """
        iparent = i // 2
        while self._arr[i] > self._arr[iparent] and i > 1:
            # swap
            (self._arr[i], self._arr[iparent]) = (self._arr[iparent], self._arr[i])
            self.heapify_up(iparent)

    def poll(self, i=0):
        """
        Get maximum element and remove it from the heap
        """

        # if self._arr[i]

    def heapify(self):
        """
        Heapify - move the root down to it's place
        """
