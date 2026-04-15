class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        a = 0
        b = 0
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b)
        }
        value = 0
        res = []

        for i in range(len(tokens)):
            if tokens[i] not in operators:
                res.append(tokens[i])
            else:
                action = operators[tokens[i]] 

                b = int(res.pop()) 
                a = int(res.pop())
                
                value = action(a, b)
                res.append(int(value))

        return int(res[0])