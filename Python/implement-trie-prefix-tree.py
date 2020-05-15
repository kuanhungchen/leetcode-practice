class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        now = self.trie

        for c in word:
            if c not in now:
                now[c] = {'#': False}
            now = now[c]
        now['#'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """

        now = self.trie

        for c in word:
            if c not in now:
                return False
            now = now[c]
        return now['#']

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """

        now = self.trie
        for c in prefix:
            if c not in now:
                return False
            now = now[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
