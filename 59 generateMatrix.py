#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/20 1:45 PM
"""


from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        """
        按模拟的顺利遍历即可
        :param n:
        :return:
        """
        cur_row, cur_col = 0, 0
        status = 0
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        for val in range(1, n*n+1):
            matrix[cur_row][cur_col] = val
            if status == 0:
                if cur_col == n-1-cur_row:
                    status = 1
                    cur_row += 1
                else:
                    cur_col += 1
            elif status == 1:
                if cur_row == cur_col:
                    status = 2
                    cur_col -= 1
                else:
                    cur_row += 1
            elif status == 2:
                if cur_col ==n-1-cur_row:
                    status = 3
                    cur_row -= 1
                else:
                    cur_col -= 1
            else:
                if cur_row == cur_col+1:
                    status = 0
                    cur_col += 1
                else:
                    cur_row -= 1
        return matrix
