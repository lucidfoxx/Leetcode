class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        ans = [i*i for i in nums]
        ans.sort()
        return ans