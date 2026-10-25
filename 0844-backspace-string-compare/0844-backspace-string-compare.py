class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        l1 = []
        t = list(t)
        l2 = []

        for i in s:
            if i == "#":
                if l1:
                    l1.pop()
            else:
                l1.append(i)

        for j in t:
            if j == "#":
                if l2:
                    l2.pop()
            else:
                l2.append(j)

        return l1 == l2