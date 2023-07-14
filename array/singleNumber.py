nums = [1, 1, 3, 5, 5]
i = 0
while(i<len(nums)):
    if(nums[i]==nums[i+1]):
        i+=2
    else:
        break
print(nums[i])