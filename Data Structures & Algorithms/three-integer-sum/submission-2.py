class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        
        for n in range(len(nums) - 2):
            # OPTIMIZATION: Stop if the smallest number is > 0
            if nums[n] > 0:
                break
                
            if n > 0 and nums[n] == nums[n - 1]:
                continue
            
            l, r = n + 1, len(nums) - 1
            while l < r:
                three_sum = nums[n] + nums[l] + nums[r]
                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    ans.append([nums[n], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return ans