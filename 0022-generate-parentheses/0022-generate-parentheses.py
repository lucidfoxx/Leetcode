class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        ansArr = []

        def recurse( st , open , close):
            if len(st) == n*2:
                ansArr.append(st)
                return
            
            if open < n:
                recurse(st + "(" , open+1, close)
            
            if close < open:
                recurse(st + ")" , open , close + 1)
            
        recurse("" , 0 , 0)
        return ansArr