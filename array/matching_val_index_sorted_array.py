nums = [1, 3, 5, 6]
target = 5
l = len(nums)
i = -1
for i in range(l):
    il = i
    ir = i+1
    if(nums[il]==target):
        break
    if(target<=nums[ir]):
        i = i + 1
        break

print(i)