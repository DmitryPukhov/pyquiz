from typing import List


class BinarySearch:
    @staticmethod
    def find_greater(items: List[int], x: int) -> int:
        if not items or x is None:
            return None
        lo = 0
        high = len(items) - 1
        last = items[high] if items[high] > x else None
        while lo < high:
            mid = (lo + high) // 2
            if items[mid] > x:
                last = items[mid]
                high = mid - 1
            else:
                lo = mid + 1
        if items[high] > x:
            last = items[high]
        return last

    @staticmethod
    def find_ge(items: List[int], x: int) -> int:
        if not items or x is None:
            return None
        lo = 0
        high = len(items) - 1
        last = items[high] if items[high] > x else None
        while lo < high:
            mid = (lo + high) // 2
            if items[mid] >= x:
                last = items[mid]
                high = mid - 1
            else:
                lo = mid + 1
        if items[high] >= x:
            last = items[high]
        return last

    @staticmethod
    def find_index(items: List[int], x: int) -> int:
        """
        Find index of item in sorted list using BS
        """
        if not items or not x:
            return -1
        items.sort()
        lo = 0
        high = len(items) - 1
        while lo <= high:
            mid = (lo + high) // 2
            if items[mid] > x:
                high = mid - 1
            elif items[mid] < x:
                lo = mid + 1
            else:
                return mid
        return -1

    @staticmethod
    def find_le(items: List[int], x: int) -> int:
        """
        Find item less or equal given
        """
        if not items or not x:
            return -1
        items.sort()
        lo = 0
        high = len(items) - 1
        lastless = items[0] if items[0] < x else None
        while lo <= high:
            mid = (lo + high) // 2
            if items[mid] == x:
                return items[mid]
            if items[mid] > x:
                high = mid - 1
            elif items[mid] < x:
                lastless = items[mid]
                lo = mid + 1
        return lastless

    @staticmethod
    def find_less(items: List[int], x: int) -> int:
        """
        Find item less or equal given
        """
        if not items or not x:
            return -1
        items.sort()
        lo = 0
        high = len(items) - 1
        lastless = items[0] if items[0] < x else None
        while lo <= high:
            mid = (lo + high) // 2
            if items[mid] >= x:
                high = mid - 1
            elif items[mid] < x:
                lastless = items[mid]
                lo = mid + 1
        return lastless
