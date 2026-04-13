class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sorting is step #1
        ans = []

        for n in range(len(nums) - 2):

            if n > 0 and nums[n] == nums[n - 1]:
                continue
            
            l = n + 1
            r = len(nums) - 1

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

        return []