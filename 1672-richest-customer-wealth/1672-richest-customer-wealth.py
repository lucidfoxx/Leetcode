class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        arr = []
        for i in accounts:
            arr.append(sum(i))
        return max(arr)
