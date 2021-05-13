#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/13 10:44 上午
"""

from typing import List


class Solution:

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        动态规划
        :param triangle:
        :return:
        """
        for row in range(len(triangle)-1):
            for col in range(len(triangle[row+1])):
                if col == 0:
                    triangle[row+1][col] += triangle[row][col]
                elif col == len(triangle[row+1])-1:
                    triangle[row+1][col] += triangle[row][col-1]
                else:
                    triangle[row+1][col] += min(triangle[row][col-1], triangle[row][col])
        return min(triangle[-1])
