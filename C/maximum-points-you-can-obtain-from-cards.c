int maxScore(int* cardPoints, int cardPointsSize, int k){
    int i;
    int best, res;
    for (i = 0, res = 0; i < k; ++i) res += cardPoints[i];
    for (i = 1, best = res; i < k + 1; ++i) {
        res = res - cardPoints[k - i] + cardPoints[cardPointsSize - i];
        if (res > best) best = res;
    }

    return best;
}
