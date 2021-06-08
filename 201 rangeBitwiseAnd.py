#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/7 11:39 上午
"""


class Solution:

    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        """
        两种思路：位移，Brian Kernighan 算法
        :param m:
        :param n:
        :return:
        """
        while m < n:
            n = n & (n-1)
        return n
