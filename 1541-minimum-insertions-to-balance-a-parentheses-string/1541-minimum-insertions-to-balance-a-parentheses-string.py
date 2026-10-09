class Solution:
    def minInsertions(self, s: str) -> int:
        close = 0
        ans = 0 
        for ch in s:
            if ch == "(":
                close+= 2 
                if close % 2 == 1:
                    ans += 1
                    close -=1
            else:
                close -= 1
                if close < 0:
                    ans += 1
                    close = 1
        return close + ans 