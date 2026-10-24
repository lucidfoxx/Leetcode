class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s1 = sorted(list(s))
        s2 = sorted(list(t))
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                return s2[i]
        return s2[-1]