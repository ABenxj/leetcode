#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/23 3:18 PM
"""


from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        思路一：记录要赋值给0的行号，列号，然后填充； 思路二：用第一行和第一列代替记录，可以节省空间消耗；
        :param matrix:
        :return:
        """
        """
        Do not return anything, modify matrix in-place instead.
        """
        status = [False, False]
        for val in matrix[0]:
            if val == 0:
                status[0] = True
                break
        for val in matrix:
            if val[0] == 0:
                status[1] = True
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                matrix[i] = [0 for _ in matrix[i]]
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for row in range(len(matrix)):
                    matrix[row][j] = 0
        if status[0]:
            matrix[0] = [0 for _ in matrix[0]]
        if status[1]:
            for row in range(len(matrix)):
                matrix[row][0] = 0
