class Solution:
    def containsDuplicate(self, nums):
        count = Counter(nums)

        for key in count:
            if count[key] > 1:
                return True
            
        return False
