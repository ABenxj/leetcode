#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/21 2:10 PM
"""


import functools


class Solution:
    @functools.lru_cache()
    def uniquePaths(self, m: int, n: int) -> int:
        """
        递归的思想，不过注意使用缓存，不然会大量重复计算，超时
        :param m:
        :param n:
        :return:
        """
        if m == 1 or n == 1:
            return 1
        return self.uniquePaths(m-1, n) + self.uniquePaths(m, n-1)

    def uniquePaths_2(self, m: int, n: int) -> int:
        """
        动态规划思想
        :param m:
        :param n:
        :return:
        """
        ans = [[1 for _ in range(n)] for _ in range(m)]
        for row in range(1, m):
            for col in range(1, n):
                ans[row][col] = ans[row-1][col] + ans[row][col-1]
        return ans[-1][-1]
