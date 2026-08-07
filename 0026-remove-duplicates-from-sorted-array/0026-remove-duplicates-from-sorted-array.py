class Solution:
    def removeDuplicates(self, nums: List[int]):
        nums[:]= sorted(set(nums))
        return len(nums)