class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        distance = 0
        max_area = 0
        
        while l < r:
            if heights[l] > heights[r]:
                distance = abs(l - r)
                if max_area < distance * heights[r]:
                    max_area = distance * heights[r]
                r -= 1

            elif heights[r] > heights[l]:
                distance = abs(l - r)
                if max_area < distance * heights[l]:
                    max_area = distance * heights[l]
                l += 1

            else:
                distance = abs(l - r)
                if max_area < distance * heights[r]:
                    max_area = distance * heights[r]
                r -= 1
                l += 1
                
        
        return max_area