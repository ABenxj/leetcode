#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/19 11:10 AM
"""


from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        递归的思想， 每次遍历最外圈，剩下的递归就好，注意边界条件； 另一种思路，按照螺旋规则，依次遍历即可。
        :param matrix:
        :return:
        """
        if len(matrix) == 1 or len(matrix[0]) == 1:
            return [x for row in matrix for x in row]
        m, n = len(matrix), len(matrix[0])
        ans = matrix[0] + [row[-1] for row in matrix[1:m-1]] + matrix[-1][::-1] + [row[0] for row in matrix[m-2:0:-1]]
        if m == 2 or n == 2:
            return ans
        return ans+self.spiralOrder([row[1:-1] for row in matrix[1:-1]])
