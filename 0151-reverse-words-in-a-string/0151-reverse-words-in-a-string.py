class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        revs = ""
        for i in words[::-1]:
            revs += i + " "
        return revs[0:len(revs)-1]