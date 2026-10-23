class Solution:
    def removeDuplicateLetters(self, s: str) -> str: 
        l = dict()
        stack = []
        visited = set()
        for i in range(len(s)):
            l[s[i]] = i
        
        for i in range(len(s)):
            if s[i] not in visited:
                while (stack and stack[-1] > s[i] and l[stack[-1]] > i):
                    visited.remove(stack.pop())

                stack.append(s[i])
                visited.add(s[i])
        return "".join(stack)