#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/13 8:54 上午
"""

from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        """
        递归或者动态规划即可
        :param numRows:
        :return:
        """
        if numRows == 1:
            return [[1]]
        ans = self.generate(numRows - 1)
        cur_level = [1]
        for i in range(len(ans[-1]) - 1):
            cur_level.append(ans[-1][i] + ans[-1][i + 1])
        cur_level.append(1)
        ans.append(cur_level)
        return ans
