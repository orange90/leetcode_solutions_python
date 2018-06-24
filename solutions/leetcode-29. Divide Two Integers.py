class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        positive = (dividend < 0) == (divisor < 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        res = 0
        while dividend >= divisor:
            temp_divisor, i = divisor, 1
            while dividend >= temp_divisor:
                dividend = dividend - temp_divisor
                res += i
                i = i << 1
                temp_divisor = temp_divisor << 1
        res = res if positive else -res
        return max(min(2147483647, res), -2147483648)  # prevent overflow


