int longestCommonSubsequence(char * text1, char * text2){
    int i, j;
    int m, n;
    for (i = 0, m = 0; text1[i] != '\0'; ++i) {
        ++m;
    }
    for (i = 0, n = 0; text2[i] != '\0'; ++i) {
        ++n;
    }

    int dp[m + 1][n + 1];
    for (i = 0; i < m + 1; ++i) {
        for (j = 0; j < n + 1; ++j) {
            if (i == 0 || j == 0) dp[i][j] = 0;
            else {
                if (text1[i - 1] == text2[j - 1]) {
                    dp[i][j] = dp[i - 1][j - 1] + 1;
                } else {
                    if (dp[i][j - 1] > dp[i - 1][j]) dp[i][j] = dp[i][j - 1];
                    else dp[i][j] = dp[i - 1][j];
                }
            }
        }
    }
    return dp[m][n];
}
