class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        sum = n
        for i in range(n - 1):
            for j in range(i+1 , n):
                sum+= len(set(nums[i:j+1])) ** 2
        return sum
