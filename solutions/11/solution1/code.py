class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0

        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = (j - i) * min(height[i], height[j])
                res = max(res, area)
                
        return res