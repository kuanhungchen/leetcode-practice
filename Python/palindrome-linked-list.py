# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        # too hard, copy from others
        fast = slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next

        pre = None
        while slow is not None:
            tmp = slow
            slow = slow.next
            tmp.next = pre
            pre = tmp

        while pre is not None:
            if pre.val != head.val:
                return False
            pre = pre.next
            head = head.next

        return True
