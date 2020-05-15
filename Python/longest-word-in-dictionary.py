class Solution:
    def longestWord(self, words):
        self.trie = {}

        def insert(word):
            now = self.trie
            for c in word:
                if c not in now:
                    now[c] = {'#': False}
                now = now[c]
            now['#'] = True

        def search(word):
            now = self.trie
            for c in word:
                if '#' in now and not now['#']:
                    return False
                now = now[c]
            return now['#']

        for word in words:
            insert(word)

        ans = ""
        for word in words:
            if search(word) and (len(word) > len(ans) or (len(word) == len(ans) and word < ans)):
                ans = word

        return ans
