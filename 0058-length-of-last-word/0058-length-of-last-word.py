class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        arr = " ".join(s.split()).split(" ")
        return len(arr[-1])