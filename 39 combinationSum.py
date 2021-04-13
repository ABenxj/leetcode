#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/13 1:16 PM
"""


from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        深度搜索(回溯法), 注意数组的排序，逆序能减少无效搜索次数，更快；
        :param candidates:
        :param target:
        :return:
        """
        ans = []
        candidates.sort(reverse=True)

        def backtrace(candidates, target, order):
            """
            回溯递归函数
            :param candidates:
            :param target:
            :param order:
            :return:
            """
            if target > 0:
                for i, val in enumerate(candidates):
                    backtrace(candidates[i:], target-val, order+[val])
            else:
                if target == 0:
                    ans.append(order)
                return None
        backtrace(candidates, target, [])
        return ans
