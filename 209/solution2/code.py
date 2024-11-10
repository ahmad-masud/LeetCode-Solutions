def minSubArrayLen(self, target: int, nums: List[int]) -> int:
    l = 0
    prefix_sum = 0
    res = float('inf')

    for r in range(len(nums)):
        prefix_sum += nums[r]

        while prefix_sum >= target:
            res = min(res, r - l + 1)
            prefix_sum -= nums[l]
            l += 1

    return res if res != float('inf') else 0