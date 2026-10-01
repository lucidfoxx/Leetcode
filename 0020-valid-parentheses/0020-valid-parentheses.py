class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = []
        for i in s:
            if len(stack) == 0:
                if i == "(" or i == "[" or i == "{":
                    stack.append(i)
                else:
                    return False
            else:
                if i == "(" or i == "[" or i == "{":
                    stack.append(i)
                elif i == ")":
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                elif i == "]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                elif i == "}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
        if len(stack) == 0:
            return True
        return False