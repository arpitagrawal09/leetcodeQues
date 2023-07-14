class Solution:
    def containsDuplicate(self, nums):
        i = 0
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i]==nums[i+1]):
                break
            if(i==len(nums)-2):
                return True
            else:
                return False

#nums = [1, 3, 4, 8]
#nums = [1, 3, 3, 4, 8]
nums = [1, 1, 3, 4, 3, 8]

sol = Solution()
bool = sol.containsDuplicate(nums)
print(bool)