class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []  

        for i, j in enumerate(temperatures):
            while stack and j > stack[-1][0]:
                First_pop, Second_pop = stack.pop()
                res[Second_pop] = i - Second_pop
            stack.append((j, i))
        return res