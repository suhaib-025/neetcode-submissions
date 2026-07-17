class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)

        bucket = [[] for i in range(len(nums)+1)]

        for n, count in hashmap.items():
            bucket[count].append(n)

        res = []
        for i in range(len(bucket)-1,-1,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res