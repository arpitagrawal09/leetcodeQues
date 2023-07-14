class Solution:
    def summaryRanges(self, nums) :
        i = 0
        j = 0
        l = len(nums)
        for i in range(l-1):
            for j in range(i , l):
                eleCurrent = nums[i]
                eleNext = nums[j]
                if((eleCurrent + 1) == eleNext):
                    j+=1
                else:
                    addRange(i, j)
   
    def addRange(i, j):
        if(i==j):
            numsRange.append()