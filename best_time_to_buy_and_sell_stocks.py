class BestTimetoBuyandSellStocks:
    def maxProfit(self, prices: List[int]) -> int:
        # Track minimum price and maximum profit
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            # Calculate profit if selling on this day
            profit = price - min_price
            # Update maximum profit if this profit is greater
            max_profit = max(profit, max_profit)
            # Update minimum price seen so far
            min_price = min(price, min_price)

        return max_profit
