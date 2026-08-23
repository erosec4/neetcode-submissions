class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # Sort (inc.) because don't care about indices
        triplets = []

        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                # Skip dupes
                continue
            
            target = -(val)
            l = i + 1
            r = len(nums) - 1

            # 2SUM on rest of array
            while l < r:
                if nums[l] + nums[r] > target:
                    # Decrement R ptr to get smaller sum
                    r -= 1
                elif nums[l] + nums[r] < target:
                    # Increment L ptr to get larger sum
                    l += 1
                else:
                    triplets.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return triplets
        