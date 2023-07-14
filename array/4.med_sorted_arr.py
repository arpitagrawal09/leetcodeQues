class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        nums = nums1 + nums2
        nums.sort()
        #print(arr)
        l = len(nums)

        isEven = False
        if(l%2==0):
            isEven = True

        median = 0
        if(isEven):
            i_Right = int(l/2) 
            i_Left = i_Right - 1
            avg = (nums[i_Left] + nums[i_Right])/2
            median = avg
        else:
            median = nums[int(l/2)]

        return median 