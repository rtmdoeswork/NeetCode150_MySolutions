class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        maxarray = [0] * len(temperatures)
        for index, value in enumerate(temperatures):
            if not stack:
                stack.append(index)
            else:
                while stack and temperatures[stack[-1]] < value:
                    finind = stack.pop()
                    maxarray[finind] = index - finind
                stack.append(index)
        return maxarray