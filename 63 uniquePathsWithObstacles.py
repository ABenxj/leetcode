#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/21 2:56 PM
"""


import functools
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        递归思想
        :param obstacleGrid:
        :return:
        """
        @functools.lru_cache()
        def recur(m, n):
            if m == 0 or n == 0 or obstacleGrid[m-1][n-1] == 1:
                return 0
            if m == 1 and n == 1:
                return 1
            else:
                return recur(m-1, n) + recur(m, n-1)
        return recur(len(obstacleGrid), len(obstacleGrid[0]))

    def uniquePathsWithObstacles_2(self, obstacleGrid: List[List[int]]) -> int:
        """
        动态规划思想
        :param obstacleGrid:
        :return:
        """
        if obstacleGrid[0][0] == 1:
            return 0
        row, col = len(obstacleGrid), len(obstacleGrid[0])
        ans = [[0 for _ in range(col+1)] for _ in range(row+1)]
        ans[0][1] = 1
        for r_i in range(1, row+1):
            for c_i in range(1, col+1):
                if obstacleGrid[r_i-1][c_i-1] == 1:
                    ans[r_i][c_i] = 0
                else:
                    ans[r_i][c_i] = ans[r_i-1][c_i] + ans[r_i][c_i-1]
        return ans[-1][-1]
