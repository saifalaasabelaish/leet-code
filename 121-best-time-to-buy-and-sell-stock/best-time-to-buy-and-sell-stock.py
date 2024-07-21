class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price = prices[0]
        max_prof = 0
        for i in range(len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]

            elif prices[i] - buy_price > max_prof:
                max_prof = prices[i] - buy_price
        return max_prof
        