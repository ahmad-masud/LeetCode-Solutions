class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(i: int, curr: List[int]) -> None:
            if i == len(nums):
                res.append(curr)
                return

            backtrack(i + 1, curr + [nums[i]])
            backtrack(i + 1, curr)

        backtrack(0, [])
        return res