class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        maxCandies = max(candies)
        result = []
        for i in candies:
            result.append(maxCandies <= (i + extraCandies))
        return result