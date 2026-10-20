
class Solution:
    def sortableIntegers(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        arr = self.divisors(n)
        sortedNums = sorted(nums)
        ans = 0

        for k in arr:
            possible = True

            for i in range(0, n, k):
                chunk = nums[i:i+k]
                target = sortedNums[i:i+k]

                if sorted(chunk) != target:
                    possible = False
                    break

                if chunk == target:
                    continue

                drops = 0
                pos = 0

                for j in range(k - 1):
                    if chunk[j] > chunk[j + 1]:
                        drops += 1
                        pos = j + 1

                if drops != 1:
                    possible = False
                    break

                if chunk[pos:] + chunk[:pos] != target:
                    possible = False
                    break

            if possible:
                ans += k

        return ans

    def divisors(self, n):
        arr = []

        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                arr.append(i)

                if i != n // i:
                    arr.append(n // i)

        arr.sort()
        return arr
