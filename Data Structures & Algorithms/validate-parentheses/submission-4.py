class Solution:
    def isValid(self, s: str, stack=None, i=0) -> bool:
        lookup = {")": "(", "}": "{", "]": "["}
        if stack is None:
            stack = []

        if i == len(s):
            return stack == []

        if s[i] in "{[(":
            stack.append(s[i])
            return self.isValid(s, stack, i + 1)

        if s[i] in ")}]":
            if not stack:
                return False
            if stack[-1] == lookup[s[i]]:
                stack.pop()
                return self.isValid(s, stack, i + 1)
            else:
                return False

        return self.isValid(s, stack, i + 1)