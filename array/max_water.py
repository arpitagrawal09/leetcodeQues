#height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
height = [4, 9, 23]

maxArea = -46329
expanse = len(height)
b = 0
l = 0
currArea = 0

""" for i in range(expanse):
    for j in range(expanse):
        l = j - i
        if(height[j]>=height[i]):
            b = height[i]
        else:
            b = height[j]
        currArea = l * b
        if(currArea > maxArea):
            maxArea = currArea
        #print(maxArea)
print(maxArea) """

""" i=0
j=0
while((i>=0) & (i<expanse)):
    while((j>i) & (j<expanse)):
        l = j - i
        if(height[j]>=height[i]):
            b = height[i]
        else:
            b = height[j]
        currArea = l * b
        if(currArea > maxArea):
            maxArea = currArea
        print(maxArea)
        j+=1
    i+=1 """
#print(maxArea)

class Solution:
    def maxArea(self, height) -> int:
        maxarea = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                width = right - left
                maxarea = max(maxarea, min(height[left], height[right]) * width)

        return maxarea
    print(area)