class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF

        while b:

            carry = (a & b) << 1

            a  = (a ^ b) & mask

            b = carry & mask
        
        max_int = 0x7FFFFFFF
        if a <= max_int:
            return a
        else:
            return ~(a ^ mask)