class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        memory = set()
        for i in range(len(nums)):
            if nums[i] in memory:
                return True
            
            memory.add(nums[i])

            if len(memory) > k:
                memory.remove(nums[i-k])
        return False