class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num,0)
        
        sorted_freq = {}
        sorted_freq = sorted(freq.items(),key =lambda x:x[1], reverse = True)

        res = []
        for n in range(k):
            res.append(sorted_freq[n][0])

        return res
            