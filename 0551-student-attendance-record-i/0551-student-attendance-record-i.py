class Solution:
    def checkRecord(self, s: str) -> bool:
        absent = 0
        for i in s:
            if i == 'A':
                absent += 1
        if absent >= 2 :
            return False
        return self.checkLate(s)
    def checkLate(self , s : str) -> bool:
        for i in range(0 , len(s) - 2):
            if s[i] == 'L' and s[i+1] == 'L' and s[i+2]== 'L':
                return False
        return True
            
