#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/22 1:58 PM
"""


import functools


class Solution:
    @functools.lru_cache()
    def climbStairs(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        return 1 if n <= 1 else self.climbStairs(n-1) + self.climbStairs(n-2)

    def climbStairs_dp(self, n: int) -> int:
        """

        :param n:
        :return:
        """
        pre, cur = 0, 1
        for _ in range(n):
            pre, cur = cur, pre + cur
        return cur
