class NumArray:

    def __init__(self, nums) :
        self.nums = nums

    def sumRange(self, left, right):
        sum = 0
        for i in range(left, right+1):
            sum+=self.nums[i]

        return sum

rankArray = [3, 1, 5, 3, 8, 7]
objArray = NumArray(rankArray)
sum = objArray.sumRange(1, 3)
print(sum)