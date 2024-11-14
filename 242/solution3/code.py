class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1

        for c in t:
            if c not in count or count[c] == 0:
                return False
            
            count[c] -= 1

        for v in count.values():
            if v != 0:
                return False

        return True