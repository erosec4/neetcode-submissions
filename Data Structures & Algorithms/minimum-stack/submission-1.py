class MinStack:

    def __init__(self):
        self.s = []
        self.m = [] # extra stack for prefixes (min corr. to each val)

    def push(self, val: int) -> None:
        self.s.append(val)
        
        # Add appropriately to m stack (compare curr min and val)
        if self.m and self.m[-1] < val:
            self.m.append(self.m[-1])
        else:
            self.m.append(val)

        return

    def pop(self) -> None:
        val = self.s.pop()
        self.m.pop()
        return

    def top(self) -> int:
        return self.s[-1]

    def getMin(self) -> int:
        return self.m[-1]
        
