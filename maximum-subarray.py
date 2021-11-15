def maxSubArray(nums):
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    # find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

    sum = None
    for i in range(len(nums)):
        current_sum = nums[i]

        if sum is None or current_sum > sum: sum = current_sum

        for j in range(i+1, len(nums)):
            current_sum += nums[j]
            if current_sum > sum: sum = current_sum
    return sum

print(maxSubArray())