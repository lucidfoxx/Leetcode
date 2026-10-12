class Solution:
    def countKeyChanges(self, s: str) -> int:
        t = s.lower()
        prev  = "s[0]"
        count = 0
        for i in t:
            if i != prev:
                count += 1
            prev = i
        return count and count - 1
            