# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        now = head
        while now:
            while now.next and now.val == now.next.val:
                now.next = now.next.next
            now = now.next
        return head
