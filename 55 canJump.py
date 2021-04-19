#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/19 11:35 AM
"""


from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        贪心算法，每次算出当前最远距离，如果当前位置超过最远距离，则返回False， 否则，更新最远距离，对比是最远距离是否超过最终位置。
        :param nums:
        :return:
        """
        cur_max = 0
        for i, val in enumerate(nums):
            if i > cur_max:
                return False
            elif cur_max <= i+val:
                cur_max = i+val
                if cur_max >= len(nums)-1:
                    return True
