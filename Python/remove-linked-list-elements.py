# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        ans = ListNode(-1)
        pre = ans
        while head:
            if head.val != val:
                pre.next = ListNode(head.val)
                pre = pre.next
            head = head.next
        return ans.next
