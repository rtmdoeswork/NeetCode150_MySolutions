class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = nums
        t = target
        index = 0
        index1 = 1

        while True:
            if nums[index] + nums[index1] == t and index != index1:
                combine = [index, index1]
                return combine
            elif True:
                index1 += 1
                if index1 == len(nums):
                    index1 = 1
                    index1 += 1
                    index += 1
            else:
                continue