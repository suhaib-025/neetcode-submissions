class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = []
        for i in range(len(nums)):
            x.append([nums[i],i])
        x.sort()
        i,j=0,len(nums)-1
        while i<j:
            cur = x[i][0] + x[j][0]
            if cur == target:
                return [min(x[i][1],x[j][1]),max(x[i][1],x[j][1])]
            elif cur < target:
                i +=1
            else:
                j -=1
        return []