# 1672. Richest Customer Wealth -> https://leetcode.com/problems/richest-customer-wealth/
# You are given an m x n integer grid accounts where accounts[i][j] is the amount of money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. 
# Return the wealth that the richest customer has.

#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        riches = []
        for i in accounts:
            wealth = sum(i)
            riches.append(wealth)
        return max(riches)