class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0,len(heights)-1
        max_storage = 0

        while left<right:
            storage = (right - left)*min(heights[left],heights[right])

            max_storage = max(max_storage,storage)
            if heights[left]<heights[right]:
                left +=1
            else:
                right -=1
        return max_storage