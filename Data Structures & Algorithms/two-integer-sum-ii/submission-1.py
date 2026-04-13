class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        n = 1
        while i in range(len(numbers)):
            if numbers[i] + numbers[n] == target:
                return [i + 1, n + 1]
            elif len(numbers) - 1 > n:
                n += 1
            else:
                n = 1
                i += 1
                n += 1