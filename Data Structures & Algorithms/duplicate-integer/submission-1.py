class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasnum = set()
        for num in nums:
            if num in hasnum:
                return True
            hasnum.add(num)

        return False
        