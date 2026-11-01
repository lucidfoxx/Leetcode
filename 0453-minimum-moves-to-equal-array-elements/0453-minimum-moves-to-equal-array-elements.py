class Solution:
    def minMoves(self, nums: list[int]) -> int:
        nums.sort()

        diff = 0 
        while nums:
            diff += (nums[-1] + diff) - (nums[0] + diff)
            nums.pop()
        
        return diff