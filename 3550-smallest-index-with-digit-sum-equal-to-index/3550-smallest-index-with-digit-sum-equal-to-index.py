class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range (len(nums)):
            if self.sumOfDigits(nums[i]) == i:
                return i 
        
        return -1 
    
    def sumOfDigits(self , num):
        sum = 0
        while num > 9:
            d = num % 10
            num //= 10
            sum += d

        return sum + num