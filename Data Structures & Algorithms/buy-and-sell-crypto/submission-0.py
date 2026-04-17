class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_buy = 0
        buy = 0
        sell = 1
        max_sell = 0

        while sell < len(prices):
            if prices[lowest_buy] > prices[buy]:
                lowest_buy = buy

            max_sell = max(max_sell, value := prices[sell] - prices[lowest_buy])

            buy += 1
            sell += 1

        if max_sell < 0:
            return 0
            
        return max_sell

        # while buy < sell:
        #     while buy < len(prices) and sell < len(prices) and prices[buy] < prices[sell]:

        #         sell_value = prices[sell] - prices[buy]
        #         buy += 1
        #         sell += 1
        #         max_sell = max(max_sell, sell_value)

        #     while buy < len(prices) and sell < len(prices) and prices[sell] < prices[buy]:

        #         sell_value = prices[sell] - prices[buy]
        #         buy += 1
        #         sell += 1
        #         max_sell = max(max_sell, sell_value)

        # if max_sell < 0:
        #     return 0
            
        # return max_sell