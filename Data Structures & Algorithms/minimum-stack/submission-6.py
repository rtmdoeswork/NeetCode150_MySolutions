class MinStack:
    def __init__(self):
        self.lst = []
        self.min_lst = []

    def push(self, val: int) -> None:
        self.lst.append(val)

        if not self.min_lst:
            self.min_lst.append(val)
        else:
            current_min = self.lst[-1]
            self.min_lst.append(min(val, self.min_lst[-1]))

    def pop(self) -> None:
        self.lst.pop()
        self.min_lst.pop()

    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.min_lst[-1]