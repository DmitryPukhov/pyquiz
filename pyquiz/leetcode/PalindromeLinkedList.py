from pyquiz.common.ListNode import ListNode


class PalindromeLinkedList:
    """
    Given a singly linked list, determine if it is a palindrome.

    Example 1:
    Input: 1->2
    Output: false

    Example 2:
    Input: 1->2->2->1
    Output: true

    Follow up:
    Could you do it in O(n) time and O(1) space?
    """

    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        # Get length
        l = self.getlen(head)

        # Reverse second part of the list
        i = 0
        n = head
        while i < l // 2:
            n = n.next
            i+=1
        n2 = self.reverse(n)

        n1 = head
        while n1 and n2:
            if n1.val != n2.val:
                return False
            n1 = n1.next
            n2 = n2.next
        return True

    def reverse(self, head: ListNode):
        n = head
        next_ = n.next
        n.next = None
        while next_:
            tmp = next_.next
            next_.next = n
            n = next_
            next_ = tmp
        return n

    def getlen(self, head: ListNode):
        """
        Get length of given linked list
        """
        n = head
        l = 0
        while n:
            l += 1
            n = n.next
        return l
