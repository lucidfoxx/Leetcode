class Solution:
    def minRotations(self, s: str) -> int:
        count = 0
        current = 0
        for i in s:
            j = int(i)
            if j != current:
                count+= min((abs(j - current)) , (10 - abs(current - j)))
                current = j
        return count