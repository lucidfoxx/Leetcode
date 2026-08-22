class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if(len(strs) == 1):
            return strs[0]
        firstWord = strs[0]
        i = 0
        letters = firstWord[0:i]
        f = True
        output = ""
        while True:
            i += 1
            if i > len(firstWord):
                return output
            letters = firstWord[0:i]
            for j in strs:
                if j[0:i] == letters:
                    f = True
                else:
                    return output
            if(f):
                output = letters

        return output
                
            