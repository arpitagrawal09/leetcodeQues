class Solution:
    def canPlaceFlowers(self, flowerbed, n) :
        flowerbed.append(0)
        flowerbed.insert(0, 0)
        l = len(flowerbed)
        maxSeats = 0
        isPossible = -1

        for i in range(1, l-1):
            left = flowerbed[i-1]
            right = flowerbed[i + 1]
            current = flowerbed[i]

            if((left==0) & (current==0) & (right==0)):
                maxSeats+=1
                flowerbed[i]=1
        
        if(maxSeats>=n): 
            isPossible = True
        else:
            isPossible = False
        return isPossible 
    
sol = Solution()
isPossible = sol.canPlaceFlowers([1,0,0,0,1], 2)
print(isPossible)


public class Solution {
    public int maximumProduct(int[] nums) {
        Arrays.sort(nums);
        return Math.max(nums[0] * nums[1] * nums[nums.length - 1], nums[nums.length - 1] * nums[nums.length - 2] * nums[nums.length - 3]);
    }
}