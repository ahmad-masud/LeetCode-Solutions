class Solution:
    def intersection(nums1: List[int], nums2: List[int]) -> int:
        set1 = set(nums1)
        set2 = set(nums2)

        return list(set1 & set2)