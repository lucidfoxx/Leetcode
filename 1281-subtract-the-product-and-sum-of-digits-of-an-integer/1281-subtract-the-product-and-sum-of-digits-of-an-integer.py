class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sod , pod = 0 , 1 
        while n > 0:
            d = n%10
            sod+= d
            pod*= d
            n//=10
        return pod - sod