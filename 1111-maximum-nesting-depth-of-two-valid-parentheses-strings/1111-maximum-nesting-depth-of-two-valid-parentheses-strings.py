class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        stack=[]
        depth=0
        for i in seq:
            if i =='(':
                stack.append(depth % 2)
                depth += 1
            elif i == ')':
                depth-=1
                stack.append(depth % 2)
                
        return stack