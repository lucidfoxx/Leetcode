class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def sod(n):
            return sum(int(i) for i in str(n))
        
        def sortingTuple(n):
            return (sod(n) , n)

        b = sorted(nums, key = sortingTuple)

        p = {}

        for i in range(len(nums)):
            p[nums[i]] = i

        swaps = 0
        for i in range(len(nums)):
            if nums[i] != b[i]:
                correct = b[i]
                j = p[correct]
                wrong = nums[i]
                nums[i] , nums[j] = nums[j] , nums[i]
                p[wrong] = j
                p[correct] = i

                swaps += 1
            
        return swaps