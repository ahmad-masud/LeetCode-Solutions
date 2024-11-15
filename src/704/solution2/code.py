class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(l, r):
            if l > r:
                return -1

            m = l + (r - l) // 2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                return binary_search(m + 1, r)
            else:
                return binary_search(l, m - 1)

        return binary_search(0, len(nums) - 1)