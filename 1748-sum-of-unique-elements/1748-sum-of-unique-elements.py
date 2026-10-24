class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        freq = {}
        sum = 0 
        for i in nums:
            if i not in freq:
                freq[i] = 0 
            freq[i] += 1
        for i in freq:
            if freq[i] == 1:
                sum+= i
        return sum