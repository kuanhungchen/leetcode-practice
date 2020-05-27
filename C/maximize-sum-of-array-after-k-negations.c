int largestSumAfterKNegations(int* A, int ASize, int K){
    int i;
    int mn_i, ans;

    while (K > 0) {
        for (i = 0, mn_i = 0; i < ASize; ++i) {
            if (A[i] < A[mn_i]) {
                mn_i = i;
            }
        }
        if (A[mn_i] != 0) {
            A[mn_i] = - A[mn_i];
        } else {
            for (i = 0, ans = 0; i < ASize; ++i) {
                ans += A[i];
            }
            return ans;
        }
        K -= 1;
    }
    for (i = 0, ans = 0; i < ASize; ++i) {
        ans += A[i];
    }
    return ans;
}
