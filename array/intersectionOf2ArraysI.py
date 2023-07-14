"""def intersection(array1, array2):
    l1 = len(array1)
    l2 = len(array2)
    array1.sort()
    array2.sort()
    i = 0
    j = 0
    inter = []
    while((i<l1) & (j<l2)):
        ele1 = array1[i]
        ele2 = array2[j]

        if(ele1 == ele2):
            i += 1
            j += 1
            inter.append(ele1)
        elif(ele1 < ele2):
            i += 1
        else:
            j += 1

    return inter

nums1 = [1, 2, 5, 5983, 4]
nums2 = [2, 5983, 4, 5, 8]
interesectionArr = intersection(nums1, nums2)
print(interesectionArr)

"""

"""def setMethodInter(array1, array2):
    a = 2 
    array1 = set(array1)
    array2 = set(array2)
    inter = []
    for ele in array1:
        if ele in array2:
            inter.append(ele)
    return inter 

nums1 = [1, 2, 5, 5983, 4]
nums2 = [2, 5983, 4, 5, 8]
interesectionArr = setMethodInter(nums1, nums2)
print(interesectionArr)"""

"""class Solution:
    def intersection(self, nums1, nums2):
        
        nums1.sort()
        nums2.sort()
        l1 = len(nums1)
        l2 = len(nums2)
        interesectionArr = []
        i = 0
        j = 0
        while i<l1 & j<l2: 
            element1 = nums1[i]
            element2 = nums2[j]
            if(element1 < element2):
                i += 1
            if(element1 == element2):
                interesectionArr.append(element1)
                j+=1
            if(element1 > element2):
                j+=1

        return interesectionArr
    
obj = Solution()
nums1 = [1, 2, 5]
nums2 = [2, 5, 8]
interesectionArr = obj.intersection(nums1, nums2)
print(interesectionArr)"""