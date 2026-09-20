class Solution:
    def reverseDegree(self, s: str) -> int:
        degree = 0 
        for i in range(len(s)):
            degree += (i+1) * (-(ord(s[i]) - 123))

        return degree