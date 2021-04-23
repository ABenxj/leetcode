#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/23 3:28 PM
"""


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        思路一：矩阵变为数组，二分查找； 思路二：二分查找，根据值解码为坐标索引； 本解法为思路二
        :param matrix:
        :param target:
        :return:
        """
        row, col = len(matrix), len(matrix[0])
        left, right = 0, row*col-1
        while left <= right:
            mid = (left+right)//2
            r_i, c_i = divmod(mid, col)
            if matrix[r_i][c_i] == target:
                return True
            elif matrix[r_i][c_i] > target:
                right = mid - 1
            else:
                left = left + 1
        return False
