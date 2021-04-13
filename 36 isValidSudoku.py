#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/13 12:32 PM
"""


from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        依次判断每行、每列、每个九宫格是否有效即可
        :param board:
        :return:
        """

        def isunique(nums: List[str]) -> bool:
            """
            判断给过来的数字是否有重复
            :param nums:
            :return:
            """
            nums_set = set()
            for item in nums:
                if item == ".":
                    continue
                elif item in nums_set:
                    return False
                else:
                    nums_set.add(item)
            return True

        for row in range(9):
            if not isunique(board[row]) or not isunique([x[row] for x in board]):
                return False
        for row in [0, 3, 6]:
            for col in [0, 3, 6]:
                if not isunique([board[row + i][col + j] for i in [0, 1, 2] for j in [0, 1, 2]]):
                    return False
        return True
