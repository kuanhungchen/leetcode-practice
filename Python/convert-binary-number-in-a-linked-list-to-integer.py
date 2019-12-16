# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getDecimalValue(self, head):
        ans, now = 0, 0
        while head:
            ans *= 2
            if head.val: ans += 1
            head = head.next
        return ans
