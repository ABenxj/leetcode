#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 3:58 PM
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        回溯法，深度搜索
        :param n:
        :return:
        """
        ans = []

        def backtrace(cur_brackets, left, right):
            """
            回溯函数
            :param cur_brackets:
            :param left:
            :param right:
            :return:
            """
            if left == 0 and right == 0:
                ans.append(cur_brackets)
                return None
            if left > 0:
                backtrace(cur_brackets+'(', left-1, right)
            if left < right:
                backtrace(cur_brackets+')', left, right-1)
        backtrace('', n, n)
        return ans
