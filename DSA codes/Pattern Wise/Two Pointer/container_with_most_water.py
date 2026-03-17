class Solution:
    def maxArea(self, height) -> int:
        i=0
        j = len(height)-1
        max1 = 0
        while i<j:
            tot = min(height[i], height[j])*(j-i)
            if tot > max1:
                max1=tot
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return max1