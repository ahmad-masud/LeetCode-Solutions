class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')

        for i in range(len(nums)):
            curr_sum = 0
            for j in range(i, len(nums)):
                curr_sum += nums[j]
                max_sum = max(max_sum, curr_sum)

        return max_sum