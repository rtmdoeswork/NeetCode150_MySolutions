class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxr = 0
        maxl = 0
        water = 0

        while l < r:
            
            if height[l] < height[r]:
                maxl = max(maxl, height[l])
                water += maxl - height[l]
                l += 1

            else:
                maxr = max(maxr, height[r])
                water += maxr - height[r]
                r -= 1
                
        return water