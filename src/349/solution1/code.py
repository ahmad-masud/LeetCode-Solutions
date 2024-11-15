class Solution:
    def intersection(nums1: List[int], nums2: List[int]) -> int:
        res = []

        for n in nums1:
            if n in nums2 and n not in res:
                res.append(n)

        return res