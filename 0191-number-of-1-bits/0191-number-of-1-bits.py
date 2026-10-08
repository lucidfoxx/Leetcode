class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0 
        st = str(bin(n))
        for i in st:
            if i == '1' :
                count += 1
        
        return count