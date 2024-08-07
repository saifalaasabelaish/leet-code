class Solution(object):
    def coinChange(self, coins, amount):
        answer = [0] + ([float('inf')] * amount)
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    answer[i] = min(answer[i], answer[i - coin] + 1)

        return -1 if answer[-1] == float('inf') else  answer[-1]

        