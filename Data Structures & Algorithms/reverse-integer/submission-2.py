class Solution:
    def reverse(self, x: int) -> int:
        Min = -214748364
        Max = 214748364

        res = 0

        while x:

            digit = int(math.fmod(x , 10))
            x = int(x / 10)

            if (res > Max or (res == Max and digit > 7)):
                return 0
            
            if (res < Min or (res == Min and digit < -8)):
                return 0

            res = (res * 10) + digit

        return res