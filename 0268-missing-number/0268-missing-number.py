class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums.sort()
        count = 0
        for i in range(len(nums)):
            if i != nums[i]:
                return i
        return len(nums)