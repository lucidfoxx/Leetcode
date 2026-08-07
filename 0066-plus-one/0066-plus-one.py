class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        if digits[-1] < 9:
            digits[-1] += 1
            return digits
        l = len(digits)
        carry = 0
        for i in range(l - 1, -1, -1):
            if digits[i] >= 9:
                digits[i] = 0
                carry = 1
                if i == 0:
                    return [1] + digits
            elif carry == 1:
                if digits[i]<9:
                    digits[i] += 1
                    carry = 0
                    return digits
        return digits
