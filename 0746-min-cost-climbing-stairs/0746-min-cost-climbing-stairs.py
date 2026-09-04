class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l = len(cost)
        prev = cost[1]
        prev2 = cost[0]

        for i in range(2, l):
            current = min(prev , prev2) + cost[i]
            prev2 , prev = prev , current 
        
        return min(prev , prev2)