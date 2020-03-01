class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isSubPath(self, head, root):
        def solve(h, r):
            # return True if the linked list starts at the current node in tree
            if not h:
                return True
            elif not r or h.val != r.val:
                return False
            else:
                return solve(h.next, r.right) or solve(h.next, r.left)

        def dfs(h, r):
            # return True if the linked list appears in any subtree
            if r.right and dfs(h, r.right):
                return True
            elif r.left and dfs(h, r.left):
                return True
            else:
                return solve(h, r)

        return dfs(head, root)
