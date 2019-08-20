import collections
class Solution:
    # hash table array-implementation
    def commonChars(self, A):
        hash_table = [0] * 26
        first = A.pop(0)
        idx = 0
        while idx < len(first):
            hash_table[ord(first[idx]) - 97] += 1
            idx += 1

        for item in A:
            idx = 0
            now = [0] * 26
            while idx < len(item):
                now[ord(item[idx]) - 97] += 1
                idx += 1
            if item == A[0]:
                hash_table = now
            else:
                hash_table = [hash_table[i] & now[i] for i in range(26)]

        ans = []

        for i in range(26):
            for j in range(hash_table[i]):
                ans.append(chr(97 + i))
        return ans


class Solution2:
    # hash table map-implementation
    def commonChars(self, A):
        first = A.pop(0)
        idx = 0
        hash_table = {}
        while idx < len(first):
            if first[idx] not in hash_table.keys():
                hash_table[first[idx]] = 1
            else:
                hash_table[first[idx]] += 1
            idx += 1

        for item in A:
            idx = 0
            now = {}
            while idx < len(item):
                if item[idx] not in now.keys():
                    now[item[idx]] = 1
                else:
                    now[item[idx]] += 1
                idx += 1
            for key in hash_table.keys():
                if key in now.keys():
                    hash_table[key] = min(hash_table[key], now[key])
                else:
                    hash_table[key] = 0

        ans = []
        for key in hash_table:
            for _ in range(hash_table[key]):
               ans.append(key)

        return ans


class Solution3:
    # much faster
    def commonChars(self, A):
        _elements = set(list(A[0]))
        r = {}
        for _element in _elements:
            tmp = []
            for item in A:
                tmp.append(item.count(_element))
            r[_element] = min(tmp)
        ans = []
        for k in r.keys():
            for _ in range(r[k]):
                ans.append(k)
        return ans
