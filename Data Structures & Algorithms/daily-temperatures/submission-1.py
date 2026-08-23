class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        warmer = [0] * len(temperatures)
        stack = [] # ALWAYS DECREASING!!!
        i = 0

        while i < len(temperatures):
            while (stack) and (temperatures[i] > list(stack[-1])[0]): # curr temp higher
                    # store curr index - popped index at popped index
                    popped = list(stack.pop())
                    warmer[popped[1]] = i - popped[1]
            
            stack.append((temperatures[i], i))
            i += 1

        return warmer
        