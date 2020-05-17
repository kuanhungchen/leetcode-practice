# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        dummy1 = odd = ListNode()
        dummy2 = even = ListNode()
        while head:
            odd.next = head
            even.next = head.next
            odd = odd.next
            even = even.next
            head = head.next.next if head.next else None
        odd.next = dummy2.next
        return dummy1.next
