class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        temp = x
        rev = 0
        while temp > 0:
            d = temp % 10
            temp //= 10
            rev = rev * 10 + d
        if rev == x:
            return True
        return False
