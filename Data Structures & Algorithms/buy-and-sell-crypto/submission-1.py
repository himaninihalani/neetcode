class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n):
            for j in range(i,n):
                if (prices[j]-prices[i])>profit and i!=j:
                    profit = (prices[j]-prices[i])
                
        return profit
        