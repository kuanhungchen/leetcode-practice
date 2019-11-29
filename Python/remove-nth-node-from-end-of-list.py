# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        slow, fast = None, head
        for _ in range(n - 1):
            fast = fast.next
        if fast.next:
            slow = head
            fast = fast.next
            while fast.next:
                slow = slow.next
                fast = fast.next
            slow.next = slow.next.next
            return head
        else:
            return head.next
