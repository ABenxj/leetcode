#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/19 10:34 AM
"""


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        和零比较大小
        :param nums:
        :return:
        """
        cur_sum, max_sum = 0, -float('inf')
        for val in nums:
            cur_sum += val
            max_sum = max(max_sum, cur_sum)
            cur_sum = max(0, cur_sum)
        return max_sum
