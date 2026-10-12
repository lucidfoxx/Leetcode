class Solution:
    def arraySign(self, nums: list[int]) -> int:
        prod = 1
        for i in nums:
            prod *= i
        
        return self.signFunc(prod)
        
    def signFunc(self , x):
        if x>0:
            return 1
        if x<0:
            return -1
        return 0