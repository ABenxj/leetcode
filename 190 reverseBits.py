#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/4 5:41 下午
"""


class Solution:

    def reverseBits(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        i = 32
        ans = 0
        while i > 0:
            i -= 1
            tmp, n = n & 1, n >> 1
            ans = ans*2+tmp
        return ans
