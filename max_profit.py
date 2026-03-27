class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices == None:
            return 0

        # Minimum price is first position in array.
        min_price = prices[0]
        max_profit = 0

        
        for price in prices:
            
            # If price is lower than any price before, update lowest price.
            if price < min_price:
                min_price = price

            # Calculate profit.
            profit = price - min_price

            if profit > max_profit:
                max_profit = profit
        
        return max_profit