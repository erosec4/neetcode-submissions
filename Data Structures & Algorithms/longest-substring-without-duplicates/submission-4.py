class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a set to check dupes
        found = set()
        
        l = 0
        longest = 0

        # 2 pointers; move L to remove dupes, move R to continue
        for r in range(len(s)):
            while s[r] in found:
                # Handle dupes
                found.remove(s[l])
                l += 1
            found.add(s[r])
            longest = max(longest, r-l+1)
        return longest


        