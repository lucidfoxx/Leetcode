class Solution:
    def firstUniqChar(self, s: str) -> int:
        n = len(s)

        for i in range(n):
            ch = s[i]
            flag = True
            for j in range(n):
                if j == i:
                    continue
                if ch == s[j]:
                    flag = False
                    break
            if flag:
                return i
            
        return -1
        
