import heapq


class Solution:
    def kClosest(self, points, K):
        # use heap
        # Time: O(NlgN), can be reduced to O(NlgK)
        # Space: O(N), can be reduced to O(K)

        def dist(point):
            return point[0] ** 2 + point[1] ** 2

        stk = []
        for point in points:
            heapq.heappush(stk, [dist(point), point])

        return [x[1] for x in heapq.nsmallest(K, stk)]


class Solution2:
    def kClosest(self, points, K):
        # use divide and conquer
        # Time: avg O(N), worst O(N^2)
        # Space: O(N)

        def dist(point):
            return point[0] ** 2 + point[1] ** 2

        dists = [[dist(x), x] for x in points]

        def findK(ds, k):
            if k == 0:
                return []
            elif len(ds) < k:
                return [d[1] for d in ds]

            pivot, left, right = ds[0], [], []
            for d in ds[1:]:
                if d[0] > pivot[0]:
                    right.append(d)
                elif d[0] <= pivot[0]:
                    left.append(d)

            if len(left) > k:
                return findK(left, k)
            elif len(left) == k:
                return [d[1] for d in left]
            else:
                return [d[1] for d in left] + [pivot[1]] + findK(right, k - len(left) - 1)

        return findK(dists, K)
