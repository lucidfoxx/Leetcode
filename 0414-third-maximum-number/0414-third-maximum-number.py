class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        s = [set(nums)]
        s = sorted(s[0])
        if len(s) < 3:
            return max(s)
        return s[-3]