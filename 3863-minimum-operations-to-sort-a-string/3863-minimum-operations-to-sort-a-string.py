class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        t = True
        for i in range(n - 1):
            if s[i] > s[i+1]:
                t = False
                break
        if t:
            return 0
        
        if n == 2:
            return -1
            
        mn = min(s)
        mx = max(s)
        if s[0] == mn or s[-1] == mx:
            return 1
        
        for i in s[1:-1]:
            if i == mn or i == mx:
                return 2

        return 3
