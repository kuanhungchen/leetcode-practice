int climbStairs(int n){
    int i;
    int dp[n + 1];
    dp[0] = 1;
    dp[1] = 1;
    for (i = 2; i < n + 1; ++i) {
        dp[i] = dp[i - 2] + dp[i - 1];
    }

    return dp[n];
}
