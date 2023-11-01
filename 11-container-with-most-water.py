class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area=0
        l=0
        r=len(height)-1
        curr_area=0

        while(l < r):
            curr_area=max(curr_area, min(height[l], height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return curr_area
