class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)

        mid = nums[n // 2]
        ans = 0

        for i in nums:
            ans += abs(i - mid)
        
        return ans