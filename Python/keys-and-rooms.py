class Solution:
    def canVisitAllRooms(self, rooms):
        unlocked = [0] + [1] * (len(rooms) - 1)  # 0: unlocked, 1: locked

        def unlock(keys):
            for key in keys:
                tmp, unlocked[key] = unlocked[key], 0
                if tmp: unlock(rooms[key])

        unlock(rooms[0])
        return not sum(unlocked)
