class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for l, r in intervals[1:]:
            if l <= res[-1][1]:
                res[-1][1] = max(r, res[-1][1])
            else:
                res.append([l, r])

        return res