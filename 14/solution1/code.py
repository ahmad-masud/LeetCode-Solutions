class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = strs[0]

        for s in strs[1:]:
            while s[:len(res)] != res:
                res = res[:-1]
                
                if not res:
                    return ""
        
        return res