class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        maxWords = 0
        for i in sentences:
            count = 1
            for j in i:
                if j == ' ':
                    count += 1 

            maxWords = max(maxWords , count)

        return maxWords 
                