class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        nsum , msum = 0 , 0
        for i in range(1 , n+1):
            if i % m != 0:
                nsum += i
            else:
                msum += i
        return nsum - msum
