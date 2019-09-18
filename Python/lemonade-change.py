class Solution:
    def lemonadeChange(self, bills):
        changes = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            if bill == 5:
                changes[5] += 1
            elif bill == 10:
                if changes[5] == 0:
                    return False
                changes[5] -= 1
                changes[10] += 1
            elif bill == 20:
                if changes[5] >= 1 and changes[10] >= 1:
                    changes[5] -= 1
                    changes[10] -= 1
                    changes[20] += 1
                elif changes[5] >= 3:
                    changes[5] -= 3
                    changes[20] += 1
                else:
                    return False
        return True
