class Solution:
    def toHex(self, num: int) -> str:
        ans = ""
        hexcodes = ['a' ,  'b' , 'c' , 'd' , 'e' , 'f']
        if num == 0:
            return '0'
        if num < 0:
            num = 2**32 + num
        while num > 0:
            d = num % 16
            num //= 16
            if d > 9:
                ans += hexcodes[d - 10]
            else:
                ans += str(d)
        return ans[::-1]