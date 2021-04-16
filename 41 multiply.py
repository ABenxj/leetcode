#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/16 9:31 AM
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        基于对应位置的乘积，再做模10处理； 有余力可以进一步考虑傅里叶变换的解法
        :param num1:
        :param num2:
        :return:
        """
        ans = [0] * (len(num1) + len(num2))
        for i, val1 in enumerate(num1):
            for j, val2 in enumerate(num2):
                ans[i + j + 1] += int(val1) * int(val2)
        for i in range(len(ans) - 1, 0, -1):
            ans[i - 1] += ans[i] // 10
            ans[i] = ans[i] % 10
        for i, val in enumerate(ans):
            if val != 0 or i == len(ans) - 1:
                break
        return ''.join([str(x) for x in ans[i:]])
