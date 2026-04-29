class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        r = k
        res = []
        window = nums[l:r]
        while r < len(nums):
            res.append(max(window))
            window.pop(0)
            window.append(nums[r])
            r += 1
            l += 1
        res.append(max(window))
        return res