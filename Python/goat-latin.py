class Solution:
    def toGoatLatin(self, s):
        goatLatinWords = []
        for num_of_a, word in enumerate(s.split(' ')):
            if word[0].lower() not in ['a', 'e', 'i', 'o', 'u']:
                word = word[1:] + word[0]
            word += "ma"
            for _ in range(num_of_a + 1): word += "a"
            goatLatinWords.append(word)
        return " ".join(goatLatinWords)
