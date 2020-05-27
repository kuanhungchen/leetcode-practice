bool divisorGame(int N){
    int i, j;
    int dp[N + 1];

    for (i = 0; i < N + 1; ++i) {
        dp[i] = 0;
    }
    for (i = 2; i < N + 1; ++i) {
        for (j = 1; j < i; ++j) {
            if (i % j == 0 && dp[i - j] == 0) dp[i] = 1;
        }
    }
    return dp[N];
}
