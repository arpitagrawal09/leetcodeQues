def twoNumberSum(array, targetSum):
    l = len(array)
    lP = 0
    rP = l-1
    pair = []
    while lP<l-1 & rP>0:
        eleLeft = array[lP]
        eleRight = array[rP]
        sumNow = eleLeft + eleRight
        if(sumNow == targetSum):
            pair = [eleLeft, eleRight]
            break
        elif( sumNow > targetSum):
            rP -= 1
        else:
            lP += 1
    return pair

"""def twoNumberSum(array, targetSum):
    # Write your code here.
    l = len(array)
    numHT = {"initialize":"ignore"}
    for num in array:
        keyList = numHT.keys()
        print(keyList)
        eleLeft = num
        eleRight = targetSum - eleLeft
        if(eleRight in numHT):
            if(numHT[eleRight]==True):
              return [eleLeft, eleRight]
        else:
            numHT.update({eleLeft : True})

nums = [2, 11, 15, 7]
target = 18
pair = twoNumberSum(nums, target)
print(pair)
"""
"""def twoSum(nums, target) :
    l = len(nums)
    pair = []
    numSet = {"initialise":"ignore"}
    for eleLeft in nums:
        eleComp = target - eleLeft
        if eleComp in numSet:
            pair = [eleLeft, eleComp]
            break
        else:
            numSet.update({eleLeft:True})
    return pair

nums = [2,7,11,15]
target = 9
pair = twoSum(nums, target)
print(pair)

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6"""

"""class Solution:
    def twoSum(self, nums, target) : 
        l = len(nums)
        i = -1
        j = -1
        for i in range(l):
            for j in range(l):
                if(i!=j):
                    sum = nums[i]+nums[j]
                    if(sum==target):
                        return [i,j]"""
                    
nums = [2,7,11,15]
target = 9
ans = [0, 1]

nums = [3,2,4]
target = 6

nums = [3,3]
target = 6


"""array = [1, 4, 2, 7, 34]
sum = 35

nums = set(array)
#print(nums)

for num1 in nums:
    num2 = sum - num1
    if num2 in nums:
        print({num1, num2})
        break"""

"""nums = {3}
nums.add(4)
nums.add(5)
print(nums)"""

