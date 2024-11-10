class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')

        for i in range(len(nums)):
            curr_sum = 0

            for j in range(i, len(nums)):
                curr_sum += nums[j]

                if curr_sum >= target:
                    res = min(res, j - i + 1)
                    break

        return res if res != float('inf') else 0