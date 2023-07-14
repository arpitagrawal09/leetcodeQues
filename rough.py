#single number 
"""
for i in range(5):
    i += 2
    print(i)
"""

""" class Solution:
    def maxProfit(self, prices):
        maxProf = 0
        for i in range(len(prices)-1):
            for j in range(i+1, len(prices)):
                thisProfit = prices[j]-prices[i]
                #print(thisProfit)
                print("In this iteration i is "+ str(i) + " and j is "+str(j))
                if(thisProfit>=maxProf):
                    maxProf = thisProfit
        if(maxProf<0):
            maxProf=0
        return maxProf 
    
stocks1 = Solution()
prices1 = [3, 2, 4]
prices2 = [1, 8, 4, 16]
pricesLeetcodeEx1 = [7, 1, 5, 3, 6, 4]
maxProfit = stocks1.maxProfit(prices1)
print(maxProfit) """

#find the median of two sorted arrays
""" arr1 = [2, 5, 6, 9, 201]
arr2 = [1, 4, 7, 9 , 271]
arr = arr1+arr2
#print(arr)
arr.sort()
print(arr) """



#learning how to insert an element into an array at a given position. succesfully used the insert method

""" parties = ['JD(S)', 'Congress', 'BJP']
#arr[3] = ['Codemongers']
parties.insert(3, "Codemongers")
print(parties) """