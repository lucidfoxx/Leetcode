class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack = []
        parenthesesList = []
        c = 0
        for i , j in enumerate(s):
            if j == '(':
                stack.append(j)
                print(stack)
            else:
                stack.pop()
                if not stack:
                    parenthesesList.append(s[c : i + 1])
                    c = i + 1      
        ans = ""
        for i in parenthesesList:
            ans += i[1:len(i)-1]
        
        return ans