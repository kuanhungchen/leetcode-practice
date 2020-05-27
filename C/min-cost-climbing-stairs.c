int minCostClimbingStairs(int* cost, int costSize){
    int i;
    int dp[costSize + 1];

    for (i = 0; i < costSize + 1; ++i) {
        dp[i] = 0;
    }
    for (i = 2; i < costSize + 1; ++i) {
        if (dp[i - 2] + cost[i - 2] < dp[i - 1] + cost[i - 1]) dp[i] = dp[i - 2] + cost[i - 2];
        else dp[i] = dp[i - 1] + cost[i - 1];
    }
    return dp[costSize];
}
