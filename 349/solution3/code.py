class Solution:
    def intersection(nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        res = set()

        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                res.add(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1

        return list(res)