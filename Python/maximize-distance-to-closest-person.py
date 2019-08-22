class Solution:
    def maxDistToClosest(self, seats):
        max_distance = seats.index(1)
        current_distance = 0
        for idx in range(len(seats)):
            if seats[idx] == 1:
                max_distance = max(max_distance, (current_distance+1)//2)
                current_distance = 0
            else:
                current_distance += 1

        max_distance = max(max_distance, current_distance)

        return max_distance
