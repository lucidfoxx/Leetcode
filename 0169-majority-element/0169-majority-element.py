class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        m = {}
        for i in nums:
            if i not in m:
                m[i] = 0
            m[i] += 1

        n = n//2
        for i , j in m.items():
            if j > n:
                return i
            
        return 0