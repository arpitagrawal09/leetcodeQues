""" j=0
i=0 

nums1=[7, 8]
nums2=[6, 9]
l1 = len(nums1)
l2 = len(nums2)

#if(nums2[j])


while((i<l1-1)&(j<l2)):
    valLeft = nums1[i]
    valRight = nums1[i+1]
    target = nums2[j]

    if(target<=valRight):
        #insert target at the next position of i
        if(i==0):
            if(target<valLeft):
                nums1.insert(0, target)
        else:
            nums1.insert(i+1, target)
            #print(j)
        j+=1
    else:
        i+=1

while(j<l2):
    #nums1[i+1]=nums2[j]
    #insert target to the right of the nums1 element
    nums1.insert(i+1, target)
    j+=1
    #i+=1

print(nums1) """

#sortedArr = [2, 5, 9, 13, 1, 14]
arr1 = [2, 5, 9]
arr2 = [1, 13, 14]
arr = arr1 + arr2
arr.sort()
#print(arr)
l = len(arr)

isEven = False
if(l%2==0):
    isEven = True

median = 0
if(isEven):
    i_Right = int(l/2) 
    i_Left = i_Right - 1
    avg = (arr[i_Left] + arr[i_Right])/2
    median = avg
else:
    median = arr[int(l/2)]

print(median)
