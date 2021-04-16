#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/16 9:11 AM
"""


from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        同46道，注意重复的临界判断条件
        :param nums:
        :return:
        """
        ans = []

        def backtrace(cur_nums, order):
            """
            递归回溯函数
            :param cur_nums:
            :param order:
            :return:
            """
            if not cur_nums:
                ans.append(order)
                return None
            for i, val in enumerate(cur_nums):
                if val not in cur_nums[:i]:
                    backtrace(cur_nums[:i] + cur_nums[i + 1:], order + [val])

        backtrace(nums, [])
        return ans