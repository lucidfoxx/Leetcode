class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(0 , n):
            for j in range(0 , n):
                if i == j:
                    continue
                else:
                    if nums[i] == nums[j]:
                        break
            else:
                return nums[i]