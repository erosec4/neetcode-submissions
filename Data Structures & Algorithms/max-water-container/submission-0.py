class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_volume = 0
        l, r = 0, len(heights) - 1

        while l < r:  
            if heights[l] < heights[r]:
                vol = (r - l) * heights[l]
                l += 1
            else:
                vol = (r - l) * heights[r]
                r -= 1

            if vol > max_volume:
                max_volume = vol

        return max_volume

        