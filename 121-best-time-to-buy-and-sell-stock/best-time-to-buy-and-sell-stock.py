class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=float('inf')
        max_price=0
        price_diff=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]
            else:
                max_price=max(max_price,prices[i]-min_price)
        return max_price

