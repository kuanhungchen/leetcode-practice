class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while True:
            c = 2
            while fast and c:
                fast = fast.next
                c -= 1
            if fast:
                slow = slow.next
            else:
                return slow if c else slow.next
