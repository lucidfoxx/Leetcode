class Solution:
    def digitSum(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k:
            return s[:]
        arr = []
        i = 0 
        while i < n:
            arr.append(s[i:i+k])
            i+= k
        ans = ""
        for i in arr:
            ans += str(self.sod(i))
        return self.digitSum(ans , k )
    
    def sod(self , s):
        sod = 0 
        for i in s:
            sod += int(i)
        return sod  