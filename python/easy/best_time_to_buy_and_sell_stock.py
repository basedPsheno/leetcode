# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_, max_, ans = 10001, -1, 0

        for price in prices:
            if price < min_:
                min_ = price
                max_ = -1
            if price > max_:
                max_ = price
            if max_ - min_ > ans:
                ans = max_ - min_

        return ans
