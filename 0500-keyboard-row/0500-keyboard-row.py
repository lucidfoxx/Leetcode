class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keys = ["qwertyuiopQWERTYUIOP" , "asdfghjklASDFGHJKL" , "zxcvbnmZXCVBNM"]
        ans = []
        for word in words:
            k1 = True
            k2 = True
            k3 = True
            for i in word:
                if i not in keys[0] :
                    k1 = False
                if i not in keys[1] :
                    k2 = False
                if i not in keys[2]:
                    k3 = False
            if k1 or k2 or k3:
                ans.append(word)
            
        return ans