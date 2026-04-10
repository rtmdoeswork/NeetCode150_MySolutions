class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, val in enumerate(nums):
            need = target - val
            if need in hashmap:
                return [hashmap[need], i]   
            hashmap[val] = i                