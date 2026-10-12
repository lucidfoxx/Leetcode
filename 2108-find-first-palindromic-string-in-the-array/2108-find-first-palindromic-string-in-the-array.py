class Solution:
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
            
        return ""
    
    def isPalindrome(self , word):
        return word[::-1] == word