class Solution:
    def stringMatching(self, words):
        ans = set()
        for word1 in words:
            for word2 in words:
                if word1 == word2:
                    continue
                if word1.find(word2) != -1:
                    ans.add(word2)

        return list(ans)
