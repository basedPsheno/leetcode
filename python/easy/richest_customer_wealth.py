# https://leetcode.com/problems/richest-customer-wealth/

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            cur_wealth = 0
            for wealth in customer:
                cur_wealth += wealth
            if cur_wealth > max_wealth:
                max_wealth = cur_wealth
        return max_wealth 
