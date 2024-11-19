class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        freq = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        return freq[:k]