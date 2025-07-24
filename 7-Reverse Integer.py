class Solution:
    def reverse(self, x):
        rev = 0
        sign = -1 if x < 0 else 1
        x = abs(x)

        while x != 0:
            rev = rev * 10 + x % 10
            x //= 10

        result = sign * rev

        if result < -2**31 or result > 2**31 - 1:
            return 0
        return result
