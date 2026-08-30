class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Bucket sort with an array where index = frequency
        # Values at index i = elements that occur i times

        count = {} # Hash to count frequency
        freq = [[] for i in range(len(nums) + 1)] # Array at each index up to maximum possible frequency = len(nums)

        for n in nums:
            count[n] = 1 + count.get(n, 0) # Get current value or return 0 of no current value; add 1
        for n, c in count.items():
            freq[c].append(n) # Put each num from count into freq at appropriate index (based on count value = frequency)

        topk = []
        for i in range(len(freq) - 1, 0, -1): # Decreasing from len to 0
            for num in freq[i]:
                if len(topk) == k:
                    return topk
                else:
                    topk.append(num)
        
        return topk