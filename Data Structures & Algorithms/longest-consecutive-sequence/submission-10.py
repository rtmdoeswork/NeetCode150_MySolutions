class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0

        nums = set(nums)
        streak = 0
        longest_streak = 0

        for i in nums:

            if i - 1 not in nums:
                j = i
                streak = 1

                while j + 1 in nums:
                    j += 1
                    streak += 1

                if streak > longest_streak:
                    longest_streak = streak

        return longest_streak