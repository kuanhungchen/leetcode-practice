int maxSubArray(int* nums, int numsSize){
    int i;
    int cur, mx;

    for (i = 0, cur = 0, mx = -1e10; i < numsSize; ++i) {
        cur += nums[i];
        if (cur > mx) mx = cur;
        if (cur < 0) cur = 0;
    }

    return mx;
}
