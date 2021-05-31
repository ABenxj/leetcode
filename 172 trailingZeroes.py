#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/31 9:34 上午
"""


class Solution:
    def trailingZeroes(self, n: int) -> int:
        """
        依次计算5、25、125等的倍数
        :param n:
        :return:
        """
        mod, ans = 5, 0
        while mod <= n:
            ans += n//mod
            mod *= 5
        return ans
