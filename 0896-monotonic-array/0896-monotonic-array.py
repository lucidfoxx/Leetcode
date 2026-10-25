class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        isInc = nums[0] <= nums[-1]
        for i in range(len(nums)-1):
            if isInc:
                if nums[i] > nums[i+1]:
                    return False
            else:
                if nums[i] < nums[i+1]:
                    return False

        return True
