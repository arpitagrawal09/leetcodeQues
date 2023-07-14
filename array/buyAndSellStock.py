# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices):
        maxProf = 0
        for i in range(len(prices)):
            for j in range(i, len(prices)):
                thisProfit = prices[j]-prices[i]
                if(thisProfit>=maxProf):
                    maxProf = thisProfit
        if(maxProf<0):
            maxProf=0
        return maxProf 
    
stocks1 = Solution()
prices1 = [3, 2, 4]
prices2 = [1, 8, 4, 16]
pricesLeetcodeEx1 = [7, 1, 5, 3, 6, 4]
maxProfit = stocks1.maxProfit(pricesLeetcodeEx1)
print(maxProfit)