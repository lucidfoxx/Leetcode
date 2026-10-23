class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        snums = sorted(nums)
        revnums = snums[::-1]
        n = len(nums)
        k = -1
        t = True
        for i in range(n):
            if snums[i] != nums[i]:
                t = False
                break
        if t:
            return 0

        t = True
        for i in range(n):
            if revnums[i] != nums[i]:
                t = False
                break

        if t:
            return 0
        for i in range(n):
            if nums[i] != snums[i]:
                k &= nums[i]
        return k 