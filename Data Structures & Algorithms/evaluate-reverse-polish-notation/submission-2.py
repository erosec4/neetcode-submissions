class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Pop last 2 ints, Operate, Push (APPEND)
        # Can have more than 2 integers in an operation,
        # and multiple operators in a row

        s = []
        for t in tokens:
            if t == "+":
                s.append(s.pop() + s.pop())
            elif t == "-":
                op2 = s.pop()
                op1 = s.pop()
                s.append(op1 - op2)
            elif t == "*":
                s.append(s.pop() * s.pop())
            elif t == "/":
                op2 = s.pop()
                op1 = s.pop()
                s.append(int(op1 / op2))
            else:
                s.append(int(t))
        
        return s.pop()
                