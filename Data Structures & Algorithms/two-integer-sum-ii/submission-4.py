class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # O(1) space --> 2 pointers
        # NUMBERS IS INCREASING

        a = 0 # L ptr
        b = len(numbers) - 1 # R ptr

        while a < b:
            if numbers[a] + numbers[b] > target:
                # Decrement R ptr to get smaller sum
                b -= 1
            elif numbers[a] + numbers[b] < target:
                # Increment L ptr to get larger sum
                a += 1
            else:
                return [a+1, b+1]
            
        