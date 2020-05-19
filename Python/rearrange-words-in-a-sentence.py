import collections


class Solution:
    def arrangeWords(self, text):
        mp = collections.defaultdict(list)
        for word in text.split(' '):
            mp[len(word)].append(word)

        ans = ""
        for k in sorted(mp.keys()):
            for word in mp[k]:
                ans = ans + " " + word
        return ans[1].upper() + ans[2:].lower()
