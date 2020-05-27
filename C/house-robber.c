int rob(int* nums, int numsSize){
    int i;
    int dp[numsSize + 1];

    if (numsSize == 0) return 0;
    else if (numsSize == 1) return nums[0];

    dp[1] = nums[0];
    dp[2] = (nums[0] > nums[1]) ? nums[0] : nums[1];

    for (i = 3; i < numsSize + 1; ++i) {
        if (nums[i - 1] + dp[i - 2] > dp[i - 1]) {
            dp[i] = nums[i - 1] + dp[i - 2];
        } else {
            dp[i] = dp[i - 1];
        }
    }

    return dp[numsSize];
}
