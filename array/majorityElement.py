class Solution:
    def majElement(self, nums):
        n = len(nums)
        halfSize = n/2
        count = 1
        for i in range(n - 1):
            if(nums[i]==nums[i+1]):
                count+=1
            else: count = 1
            if count>halfSize: break
        return nums[i]
    
nums1 = [4, 4, 3, 3, 3] #3
nums2 = [4, 7, 4]    #4
nums3 = [1, 2, 1, 3, 1, 2, 1]   #1
sol = Solution()
print(sol.majElement(nums3))

#print("It's printing")