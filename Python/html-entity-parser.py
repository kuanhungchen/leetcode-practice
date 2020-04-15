class Solution:
    def entityParser(self, text):
        ps = [[6, "&quot;", '"'],
              [6, "&apos;", "'"],
              [5, "&amp;", '&'],
              [4, "&gt;", '>'],
              [4, "&lt;", '<'],
              [7, "&frasl;", '/']]
        ans = ""
        idx = 0
        while idx < len(text):
            while idx < len(text) and text[idx] != '&':
                ans += text[idx]
                idx += 1

            replaced = False
            for p in ps:
                if idx + p[0] <= len(text) and text[idx:idx + p[0]] == p[1]:
                    ans += p[2]
                    idx += p[0]
                    replaced = True
                    break
            if not replaced and idx < len(text):
                ans += text[idx]
                idx += 1
        return ans
