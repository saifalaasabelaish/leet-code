class Solution(object):
    def coinChange(self, coins, amount):
        memo = {}

        def dfs(rem):
            if rem == 0:
                return 0
            if rem < 0:
                return float('inf')
            
            if rem in memo:
                return memo[rem]

            ans = float('inf')
            for coin in coins:
                ans = min(ans, 1 + dfs(rem - coin))

            memo[rem] = ans
            return ans

        result = dfs(amount)
        return result if result != float('inf') else -1
