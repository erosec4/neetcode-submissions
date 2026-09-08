class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window: move R while valid, then move L
        # Window length = r - l + 1

        l = 0
        longest = 0
        count = {} # Map characters to occurrences to get majority

        for r in range(len(s)):
            # Avoid error if char not in dict already
            count[s[r]] = 1 + count.get(s[r], 0) 
            
            # Valid window: window length - max(count.values()) <= k
            while (r - l + 1) - max(count.values()) > k:
                # Invalid window --> move L
                count[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
        
        return longest
            

        