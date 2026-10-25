class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        sof = 0
        t = x
        while t > 0:
            sof += t%10
            t//=10
        return sof if x % sof == 0 else -1