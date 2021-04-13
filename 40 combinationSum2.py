#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/13 1:34 PM
"""


from typing import List


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        与39题类似，注意回溯时的判断条件
        :param candidates:
        :param target:
        :return:
        """
        candidates.sort(reverse=True)
        ans = []

        def backtrace(candidates: List[int], target: int, order: List[int]) -> None:
            """
            回溯递归过程
            :param candidates:
            :param target:
            :param order:
            :return:
            """
            if target == 0:
                ans.append(order)
                return None
            elif target < 0:
                return None
            else:
                for i, val in enumerate(candidates):
                    if i == 0 or val < candidates[i - 1]:
                        backtrace(candidates[i + 1:], target - val, order + [val, ])

        backtrace(candidates, target, [])
        return ans
