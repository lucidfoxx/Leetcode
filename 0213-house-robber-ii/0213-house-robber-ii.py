class Solution:
    def rob(self, nums: List[int]) -> int:
        l = len(nums)
        if l == 0:
            return 0
        if l <=2:
            return max(nums)
        prev = nums[0]
        prev2 = max(prev , nums[1])
        for i in range( 2,l-1):
            current = max(prev + nums[i] , prev2)
            prev , prev2 = prev2 , current
        sum1 = prev2

        prev = nums[1]
        prev2 = max(prev , nums[2])

        for i in range(3 , l):
            current = max(prev + nums[i] , prev2)
            prev , prev2 = prev2 , current
        sum2 = prev2 

        return max(sum1 , sum2)