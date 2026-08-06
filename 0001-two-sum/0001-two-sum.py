class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        for i in range(length):
            x = nums[i]
            if (target - x) in (nums[0:i] + nums[i + 1 : length + 1]):
                return [i, nums.index((target - x) , i+1)]

        return []
