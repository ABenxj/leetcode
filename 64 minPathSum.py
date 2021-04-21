#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/21 3:22 PM
"""


import functools
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        """
        递归思想， 这一题中，递归方法会慢很多；
        :param grid:
        :return:
        """
        @functools.lru_cache()
        def recur(m, n):
            if m == 1 and n == 1:
                return grid[0][0]
            elif m == 0 or n == 0:
                return float('inf')
            return grid[m-1][n-1] + min(recur(m-1, n), recur(m, n-1))
        return recur(len(grid), len(grid[0]))

    def minPathSum_2(self, grid: List[List[int]]) -> int:
        """
        动态规划思想
        :param grid:
        :return:
        """
        grid = [[float('inf')]+x for x in grid]
        grid.insert(0, [float('inf')]*len(grid[0]))
        grid[0][1] = 0
        for row in range(1, len(grid)):
            for col in range(1, len(grid[0])):
                grid[row][col] += min(grid[row][col-1], grid[row-1][col])
        return grid[-1][-1]
