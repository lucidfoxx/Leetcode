class Solution:
    def countDigits(self, num: int) -> int:
        temp = num
        c = 0 
        while temp > 0:
            d = temp%10
            temp //= 10
            if num%d == 0:
                c += 1
            
        return c 