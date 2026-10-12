class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        ans = []
        for i in range(left , right + 1):
            if self.isSelfDividing(i):
                ans.append(i)
        return ans

    def isSelfDividing(self , num):
        n = num
        while(n>0):
            d = n%10
            if d == 0:
                return False
            if num%d != 0:
                return False
            n //= 10
        return True
        
        return 
