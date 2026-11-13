class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        given: integer array prices: -> int
        one buy day and one future sell day so i < j

        return max profit -> defined as sell price - buy price or 0. 0 would probably be
        a decreasing array or like all the same value

        [10, 1, 5, 6, 7, 1]
             ^        ^
        the largest profit

        simplest: all combinations which we can do a nested for loop and compare profits
        O(n^2)

        10 1 5 6 7 1
        
        b, s = 0, 1
        maxP = 0
        while s < len(prices):
            if buy < sell:
                profit = sell - buy
                maxP = max(profit, maxP)
            else:
                b = s
            b += 1
        return maxP
        
        """
        b, s = 0, 1
        maxP = 0
        while s < len(prices):
            if prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxP = max(profit, maxP)
            else:
                b = s
            s += 1
        return maxP
        