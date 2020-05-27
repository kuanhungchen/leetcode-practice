int maxProfit(int* prices, int pricesSize){
    int i;
    int now, best;

    if (pricesSize == 0) return 0;

    for (i = 1, now = prices[0], best = 0; i < pricesSize; ++i) {
        if (prices[i] - now > best) best = prices[i] - now;
        if (prices[i] < now) now = prices[i];
    }
    return best;
}
