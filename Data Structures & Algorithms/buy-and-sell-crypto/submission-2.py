class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MinPrice = 101
        MaxProfit = 0

        for i in range(len(prices)):
            if prices[i] - MinPrice > MaxProfit:
                MaxProfit = prices[i] - MinPrice

            if prices[i] < MinPrice:
                MinPrice = prices[i]
        
        return MaxProfit
