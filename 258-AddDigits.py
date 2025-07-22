class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num >= 10:
            sum_digits = 0
            for digit in str(num):
                sum_digits += int(digit)
                num = sum_digits
        return num