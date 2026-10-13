class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = [i*i for i in nums]
        n.sort()
        l = len(n)
        s = l // 2
        small = n[:s]
        big = n[s:]
        return sum(big) - sum(small)
