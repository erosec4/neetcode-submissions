class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit = largest sell - buy
        # dynamic sliding window

        max_profit = 0
        b = 0
        s = 1

        # add to sell until profit < 0, then move buy
        while s < len(prices):
            profit = prices[s] - prices[b]
            if profit > max_profit:
                max_profit = profit
            elif profit < 0:
                # Sell value < buy value; want to move b to s
                b = s
            s += 1

        return max_profit






        