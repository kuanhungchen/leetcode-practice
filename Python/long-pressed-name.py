class Solution:
    def isLongPressedName(self, name, typed):
        fast = 0
        typed_idx = 0
        while fast < len(name):
            slow = fast
            while fast < len(name) and name[fast] == name[slow]:
                fast += 1
            num = fast - slow
            while typed_idx < len(typed) and typed[typed_idx] == name[slow]:
                typed_idx += 1
                num -= 1
            if num > 0:
                return False
        return typed_idx == len(typed)
