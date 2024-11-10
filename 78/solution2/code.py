class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for n in nums:
            res += [curr + [n] for curr in res]

        return res