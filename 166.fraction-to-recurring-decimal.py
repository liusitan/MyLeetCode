#
# @lc app=leetcode id=166 lang=python3
#
# [166] Fraction to Recurring Decimal
#

# @lc code=start



import re
from unicodedata import decimal

from numpy import int_


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"
        sign = ''
        if (numerator> 0) ^ (denominator > 0):
            sign = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        int_part = str(numerator//denominator)
        

        remainder = numerator % denominator
        if remainder == 0:
            return sign + int_part
        decimal_part = ''
        i = 0
        m  ={}
        while remainder:
            remainder*=10
            if remainder in m:
                decimal_part = decimal_part[:m[remainder]] + '(' + decimal_part[m[remainder]:]+")"
                break
            m[remainder ] = i
            decimal_part += str(remainder//denominator)
            remainder%=denominator
            i+=1
        return sign+int_part+"."+decimal_part
# @lc code=end

