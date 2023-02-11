class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = sum(accounts[0])
        for customer in accounts:
            if sum(customer) > richest:
                richest = sum(customer)
        return richest
