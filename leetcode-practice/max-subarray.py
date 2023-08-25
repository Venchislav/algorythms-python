def maxSubArray(nums):
    if not nums:
        return 0

    n = max_sum = nums[0]

    for i in nums[1:]:
        n = max(i, n + i)
        max_sum = max(n, max_sum)
    return max_sum