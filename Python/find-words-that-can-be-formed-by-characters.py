class Solution:
    def countCharacters(self, words, chars):
        char_dict = {}
        for char in chars:
            try:
                char_dict[char] += 1
            except KeyError:
                char_dict[char] = 1

        ans = 0
        for word in words:
            if len(word) > len(chars):
                # this if-statement makes much improvement
                continue
            word_dict = {}
            track = 0
            for char in word:
                try:
                    word_dict[char] += 1
                except KeyError:
                    word_dict[char] = 1
            for k, v in word_dict.items():
                if k not in char_dict.keys() or char_dict[k] < v:
                    break
                else:
                    track += 1
            if len(word_dict) == track:
                ans += len(word)

        return ans
