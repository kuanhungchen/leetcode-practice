class Solution:
    def suggestedProducts(self, products, searchWord):
        products.sort()
        ans = []
        now = ""
        for c in searchWord:
            now += c
            ans.append([])
            for product in products:
                if len(ans[-1]) == 3: break
                if len(now) <= len(product) and now == product[:len(now)]: ans[-1].append(product)
        return ans
