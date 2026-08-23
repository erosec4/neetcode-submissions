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

        # if curr temp is lower/equal to s.peek --> stack temp, index
        # if curr is higher --> continue popping until s.peek is higher/equal
            # while popping: store curr index - popped index at popped index
        # push curr temp, index to stack
        # continue until curr index = len(temperatures)
        # O(n)

        # [22, 23, 20]
        # [10, 10, 10]
        # [35]
        