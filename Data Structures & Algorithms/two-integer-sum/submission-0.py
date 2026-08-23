class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        passed = {}
        for i in range (len(nums)):
            iso = target - nums[i]
            if iso in passed:
                return [passed[iso], i]
            else:
                passed[nums[i]] = i


        # Dictionary/Hash Table/Map of number : index
        # Check dict for target - nums[curr]
        # If there: return dict[target-nums[curr]], curr
        # If not: add dict[nums[curr]] = curr