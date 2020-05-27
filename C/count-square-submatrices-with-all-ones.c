int countSquares(int** matrix, int matrixSize, int* matrixColSize){
    int i, j;
    int dp[matrixSize + 1][matrixColSize[0] + 1];

    for (i = 0; i < matrixSize + 1; ++i) {
        dp[i][0] = 0;
    }
    for (i = 0; i < matrixColSize[0] + 1; ++i) {
        dp[0][i] = 0;
    }
    for (i = 1; i < matrixSize + 1; ++i) {
        for (j = 1; j < matrixColSize[0] + 1; ++j) {
            dp[i][j] = dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1] + matrix[i - 1][j - 1];
        }
    }

    int ans = 0;
    int l, edge;
    edge = (matrixSize < matrixColSize[0]) ? matrixSize : matrixColSize[0];
    for (i = 1; i < matrixSize + 1; ++i) {
        for (j = 1; j < matrixColSize[0] + 1; ++j) {
            l = 1;
            while (i - l >= 0 && j - l >= 0) {
                ans += (l * l == dp[i][j] - dp[i - l][j] - dp[i][j - l] + dp[i - l][j - l]);
                ++l;
            }
        }
    }

    return ans;
}
