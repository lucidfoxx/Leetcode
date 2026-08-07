class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums)==1:
            return 0 if target <= nums[0] else 1
        if target in nums:
            for i in range(len(nums)):
                if target == nums[i]:
                    return i
        for i in range(len(nums) - 1):
            if(i==0 and target < nums[i]):
                return 0
            if nums[i] < target and target < nums[i + 1]:
                return i + 1
        return len(nums)
