#Remove duplicates from a sorted array 
#Problem 26 page https://leetcode.com/tag/array/    51.6%   easy 

""" 1) increasing order 'nums' array 

say nums = [3, 3, 7, 18]
say nums_unique = [0, 1, 2]
length of array = 2 = k = answer 

kya - repeat hatao 
loop - bas unique pakadke sort 
        kaise pakde unique
        naya element dikhte hai record karlo(array size apne aap badhte)
        pichle element ka record rakho(element_last)
            
            num_unique = [3]
            num[1]==3 --> leave
            num_unique = [3,7]
            num_unique = [3,7,18]
            
            return num_unique

        example : nums = [65, 67, 67, 67, 82, 89, 89, 93, 93]

                i = 0 -> num_unique = [65]
                i = 1 -> element same as previous 
                        num_unique no change
                i = 2 ->

                i = 8 -> num_unique = no change
                finally
                    num_unique = [65, 67, 82, 89, 93]
                    k = 5
                    return k """

nums = [65, 67, 67, 67, 82, 89, 89, 93, 93]
#print(len(nums_unique))
lNums = len(nums)
nums_unique=[]
previous='init'
for i in range(lNums):
    value = nums[i]
    if(previous!=value):
        nums_unique.append(value)
        previous=value
print(nums_unique)
print(len(nums_unique))
