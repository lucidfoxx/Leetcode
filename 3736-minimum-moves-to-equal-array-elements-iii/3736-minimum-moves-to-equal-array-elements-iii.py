class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0 
        m = nums[-1]
        for i in nums:
            ans += m - i

        return ans