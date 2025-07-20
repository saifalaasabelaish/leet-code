class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        buy_price=prices[0]
        for i in range(1,len(prices)):
            if buy_price>prices[i]:
                buy_price=prices[i]
            elif prices[i]-buy_price>max_profit :
                max_profit=prices[i]-buy_price
        return max_profit        
