class Solution:
    def isValid(self, s: str) -> bool:

        # Stack open brackets
        # When reach a closed bracket: pop and check top of stack
            # Match --> cont.
            # Mismatch --> F
        # End of str & stack empty --> T
            # Stack not empty --> F (smth not closed)

        # Edge case e.g. ([]{})
        # Edge case: non-bracket character

        opened = {"(", "{", "["}
        closed = {")", "}", "]"}
        match = {"(": ")", "{": "}", "[":"]"}
        # OR: could use closed as the keys, and check if b in match

        open_stack = []

        for b in s:
            if b in opened:
                open_stack.append(b)
            elif b in closed:
                # ERROR: can't pop from empty stack
                if len(open_stack) == 0:
                    return False
                else:
                    if match[open_stack.pop()] != b:
                        return False
            else:
                # Non-bracket character
                return False

        if len(open_stack) == 0:
            return True
        else:
            return False
        # OR "return True if not open_stack else false"



















        # check if len is even
        if len(s) % 2 == 1:
            return False
        else:
            # CHECK IF IT'S OPENING OR CLOSING!

            ''' stack = []
            # push first half into stack
            i = 0
            while i < (len(s) / 2):
                stack.append(s[i])
                i += 1
            # pop and match with 2nd half
            while i < len(s):
                curr = str(stack.pop())
                if s[i] != curr:
                    return False
                i += 1
            return True'''



