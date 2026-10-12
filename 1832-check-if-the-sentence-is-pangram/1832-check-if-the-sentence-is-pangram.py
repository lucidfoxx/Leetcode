class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alpha = set()
        for ch in sentence:
            alpha.add(ch)
        
        return len(alpha) == 26