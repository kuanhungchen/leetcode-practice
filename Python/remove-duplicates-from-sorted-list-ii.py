# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        now = head
        _dict = {}
        while now.next:
            if now.val not in _dict.keys():
                _dict[now.val] = 1
            else:
                _dict[now.val] += 1
            now = now.next
        if now.val not in _dict.keys():
            _dict[now.val] = 1
        else:
            _dict[now.val] += 1

        nodes = [ListNode(x) for x in _dict if _dict[x] == 1]
        if len(nodes) == 0:
            return None
        if len(nodes) == 1:
            return nodes[0]
        for idx in range(len(nodes) - 1):
            nodes[idx].next = nodes[idx + 1]

        return nodes[0]


class Solution2:
    def deleteDuplicates(self, head):
        if head is None:
            return None
        if head.next is None:
            return head
        now = head
        _dict = {}
        while now.next is not None:
            if now.val not in _dict.keys():
                _dict[now.val] = 1
            else:
                _dict[now.val] += 1
            now = now.next
        if now.val not in _dict.keys():
            _dict[now.val] = 1
        else:
            _dict[now.val] += 1

        ans = pre = ListNode
        ans.next = cur = head
        while cur and cur.next:
            if _dict[cur.val] != 1:
                while cur.next and _dict[cur.next.val] != 1:
                    cur = cur.next
                pre.next = cur = cur.next
            else:
                pre, cur = cur, cur.next

        return ans.next


class Solution3:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # copy from others
        pre = ans = ListNode(float('inf'))
        ans.next = cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur = cur.next
            else:
                pre, cur = cur, cur.next
        return ans.next
