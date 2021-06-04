#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/4 5:44 下午
"""


class Solution:

    def hammingWeight(self, n: int) -> int:
        """

        :param n:
        :return:
        """

        ans = 0
        while n > 0:
            ans += n & 1
            n = n >> 1
        return ans
