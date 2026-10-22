class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len (nums)
        a , d = 1 , 1

        for i in range(1 , n):
            if (nums[i] == ( nums[i-1] + 1 ) % n):
                a += 1
            if nums[i-1] == (nums[i] + 1 ) % n:
                d += 1
        if a == n:
            if nums[0] == 0:
                return 0
            else:
                return min(n - nums[0]  , nums[0] + 2) 
            
        if d == n:
            return min(n - nums[-1]  , nums[-1] ) +  1 

        return -1 