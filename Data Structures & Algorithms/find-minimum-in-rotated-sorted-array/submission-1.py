class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        lowest = float("inf")

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] > nums[r]:
                l = m + 1
                lowest = min(lowest, nums[m])
            else:
                r = m - 1
                lowest = min(lowest, nums[m])
        return lowest