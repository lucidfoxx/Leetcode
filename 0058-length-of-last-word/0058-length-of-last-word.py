class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = s.split(' ')
        while(arr[-1] == ''):
            arr.pop(-1)
        return len(arr[-1])