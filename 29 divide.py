#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 5:13 PM
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        """
        注意通过二进制的方法减少计算量， 边界值也需要注意一下；
        :param dividend:
        :param divisor:
        :return:
        """
        sign = -1
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            sign = 1
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        divs = []
        while divisor <= dividend:
            divs.append(divisor)
            divisor += divisor
        len_divs = len(divs)
        for i, div in enumerate(divs[::-1]):
            while dividend >= div:
                ans += 2**(len_divs-i-1)
                dividend -= div
        ans = 0 - ans if sign == -1 else ans
        ans = max(-2**31, min(ans, 2**31-1))
        return ans
