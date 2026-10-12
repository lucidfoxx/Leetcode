class Solution:
    def maxSum(self, nums: List[int], k: int) -> int:
        biter = [0] *32
        for x in nums:
            for i in range(32):
                if (x >> i) & 1:
                    biter[i] += 1
        new = [0] *k
        for i in range(31,-1,-1):
            count = min(k,biter[i])
            for j in range(count):
                new[j] |=1 <<i
        ans =0
        for x in new:
            ans = (ans +x *x)% (10**9 +7)
        return ans