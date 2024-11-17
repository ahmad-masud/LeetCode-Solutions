class Solution:
    def containsDuplicate(self, nums):
        counts = {}

        for n in nums:
            if n in counts:
                return True
            
            counts[n] = 1

        return False