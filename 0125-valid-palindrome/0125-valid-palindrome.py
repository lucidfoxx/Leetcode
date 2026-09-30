class Solution:
    def isPalindrome(self, s: str) -> bool:
        formatedString = ""
        for char in s :
            if char.isalpha() or char.isnumeric():
                formatedString += char
        formatedString = formatedString.lower()
        return formatedString == formatedString[::-1]