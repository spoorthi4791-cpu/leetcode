class Solution(object):
    def maximumWealth(self, accounts):
        maximum = 0

        for i in range(len(accounts)):
            total = sum(accounts[i])

            if total > maximum:
                maximum = total

        return maximum