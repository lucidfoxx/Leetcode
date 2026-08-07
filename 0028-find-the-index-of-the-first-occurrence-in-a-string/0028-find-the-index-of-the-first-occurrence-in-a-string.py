class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            for i in range(0, len(haystack)-len(needle)+1):
                if needle[0] == haystack[i]:
                    t = True
                    for j in range(1, len(needle)):
                        if needle[j] != haystack[i + j]:
                            t = False
                            break
                    if t:
                        return i
        return -1
