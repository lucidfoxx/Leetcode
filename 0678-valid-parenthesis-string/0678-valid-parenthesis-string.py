class Solution:
    def checkValidString(self, s: str) -> bool:
        close , open = 0 , 0 
        for ch in s:
            if ch == '(':
                close += 1
                open += 1 
            elif ch == ')':
                close -= 1
                open -= 1
            else:
                close -=1 
                open += 1
            if open < 0 :
                return False
            if close < 0:
                close = 0
            
        return close == 0