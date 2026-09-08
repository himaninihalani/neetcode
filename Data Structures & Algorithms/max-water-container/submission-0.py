class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i=0
        left = 0
        right = n-1
        area = 0
        while left<right:
            width = right - left
            height = min(heights[left],heights[right])
            area = max(area , height*width)
            
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return area