class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        k = -1
        s = sorted(nums)
        n = len(nums)
        for i in range(n):
            if s[i] != nums[i]:
                k &= nums[i]
        
        if k == -1:
            return 0
        return k