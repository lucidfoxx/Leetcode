class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        esum = 0
        dsum = 0
        for i in nums:
            if i < 10:
                esum += i
                dsum += i
            else:
                esum += i
                dsum+= self.sumOfDigits(i)
        
        return abs(esum-dsum)
    
    def sumOfDigits(self , num):
        sod = 0
        while num > 0:
            sod += num%10
            num//= 10
        
        return sod