class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}

        for n in nums:
            hash_table[n] = hash_table.get(n, 0) + 1

        for n, count in hash_table.items():
            if count == 1:
                return n