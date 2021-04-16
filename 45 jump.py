#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/15 8:40 PM
"""


from typing import List


class Solution:

    def jump(self, nums: List[int]) -> int:
        """
        动态规划
        :param nums:
        :return:
        """
        jump_cnt = list(range(len(nums)))
        for i, val in enumerate(nums):
            for j in range(val):
                if i+j+1 < len(jump_cnt):
                    jump_cnt[i+j+1] = min(jump_cnt[i+j+1], jump_cnt[i]+1)
        return jump_cnt[-1]
