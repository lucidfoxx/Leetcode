class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = {}
        for i in nums:
            if i in ans.keys():
                ans[i] += 1
            else:
                ans[i] = 1
        
        for key in ans:
            if ans[key] == 1:
                return key