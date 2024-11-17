class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = float('inf')

        for n in nums:
            if abs(n) < abs(res):
                res = n
            elif abs(n) == abs(res):
                res = max(n, res)

        return res