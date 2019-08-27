class Solution:
    def numSmallerByFrequency(self, queries, words):
        word_freqs = []
        for word in words:
            _smallest = 122
            freq = 0
            for c in word:
                if ord(c) == _smallest:
                    freq += 1
                elif ord(c) < _smallest:
                    _smallest = ord(c)
                    freq = 1
            word_freqs.append(freq)
        word_freqs.sort(reverse=True)

        ans = []
        for query in queries:
            _smallest = 122
            freq = 0
            for c in query:
                if ord(c) == _smallest:
                    freq += 1
                elif ord(c) < _smallest:
                    _smallest = ord(c)
                    freq = 1
            tmp = 0
            for word_freq in word_freqs:
                if word_freq > freq:
                    tmp += 1
                    continue
                break
            ans.append(tmp)
        return ans
