class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open , answer = 0 , 0 
        for ch in s:
            if ch == '(':
                open += 1
            else:
                if open > 0:
                    open -= 1
                else:
                    answer += 1
            
        return answer + open