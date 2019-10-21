class Solution:
    def removeSubfolders(self, folders):
        folders.sort()
        _dict = {}
        for folder in folders:
            flag = True
            tmp = []
            for filename in folder.split('/'):
                tmp.append(filename)
                if tuple(tmp) in _dict:
                    flag = False
                    break
            if flag:
                _dict[tuple(tmp)] = 1
        ans = []
        for k, v in _dict.items():
            ans.append("/".join(list(k)))
        return ans
