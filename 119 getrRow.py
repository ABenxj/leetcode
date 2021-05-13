#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/13 8:58 上午
"""


from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        """
        递归或动态规划，与上一题思路基本一致
        :param rowIndex:
        :return:
        """
        if rowIndex == 0:
            return [1]
        ans = self.getRow(rowIndex - 1)
        cur_level = [1]
        for i in range(len(ans) - 1):
            cur_level.append(ans[i] + ans[i + 1])
        cur_level.append(1)
        return cur_level
