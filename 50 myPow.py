#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/17 4:04 PM
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:
        """
        直接对幂数mod2求解，也可以对采用递归的做法；
        :param x:
        :param n:
        :return:
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1/x
            n = abs(n)
        ans_part, ans_main = 1, x
        while n > 1:
            if n%2 == 1:
                ans_part *= ans_main
            if n > 1:
                ans_main = ans_main*ans_main
                n = n//2
        return ans_part*ans_main
