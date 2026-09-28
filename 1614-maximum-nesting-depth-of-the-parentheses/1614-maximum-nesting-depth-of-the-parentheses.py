class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        maxNest = 0 
        for i in s:
            if i == "(":
                stack.append("(")
            if i == ")":
                maxNest = max(maxNest , len(stack))
                stack.pop()
            
        return maxNest