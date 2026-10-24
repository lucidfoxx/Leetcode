class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        n = len(s)
        a = s[:n//2]
        b = s[n//2:]
        va , vb = 0 , 0
        for i in range(n//2):
            if a[i] in "aeiouAEIOU":
                va+= 1
            if b[i] in "aeiouAEIOU":
                vb+= 1
        return va == vb
            