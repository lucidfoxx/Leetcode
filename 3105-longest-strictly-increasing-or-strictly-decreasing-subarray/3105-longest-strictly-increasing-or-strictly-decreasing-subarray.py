class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        maxinc = 0
        maxdec = 0
        inc = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                inc += 1
            else:
                maxinc = max(maxinc , inc)
                inc = 1
        maxinc = max(maxinc , inc)
        
        dec = 1
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                dec += 1
            else:
                maxdec = max(maxdec , dec)
                dec = 1
        maxdec = max(maxdec , dec)
        
        return max(maxinc, maxdec)