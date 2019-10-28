class Solution:
    def computeArea(self, A, B, C, D, E, F, G, H):
        if A < E:
            width = C - E if G >= C >= E else G - E if C >= G >= E else 0
        else:
            width = G - A if C >= G >= A else C - A if G >= C >= A else 0
        if B > F:
            height = H - B if D >= H >= B else D - B if H >= D >= B else 0
        else:
            height = D - F if H >= D >= F else H - F if D >= H >= F else 0
        return (D - B) * (C - A) + (H - F) * (G - E) - width * height
