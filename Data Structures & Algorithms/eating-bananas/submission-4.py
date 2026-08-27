class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Each pile takes math.ceil(bananas/k) hours

        # For ceiling function
        import math

        max_pile = max(piles)
        best_k = max_pile

        if h == len(piles):
            # If each pile gets 1 hour --> return maximum
            return best_k

        else:
            # Binary search all possible k values from 1 to max pile
            l, r = 1, max_pile
            while l <= r:
                k = (l + r) // 2
                total_hours = 0
                for pile in piles:
                    total_hours += math.ceil(pile / k)
                if total_hours <= h:
                    if k < best_k:
                        best_k = k
                    # Go left
                    r = k-1
                else:
                    # Go right
                    l = k+1
            return best_k

        