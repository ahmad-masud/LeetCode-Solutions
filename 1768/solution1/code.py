class Solution:
    def mergeAlternately(self, w1: str, w2: str) -> str:
        res = []
        l = 0

        while l < len(w1) or l < len(w2):
            if l < len(w1):
                res.append(w1[l])
                
            if l < len(w2):
                res.append(w2[l])

            l += 1

        return ''.join(res)