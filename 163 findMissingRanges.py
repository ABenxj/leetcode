#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/29 7:46 上午
"""


from typing import List


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        """
        双指针法
        :param nums:
        :param lower:
        :param upper:
        :return:
        """
        left, right = lower, lower - 1
        ans = []
        for val in nums + [upper + 1]:
            if val != left:
                right = val - 1
                if left == right:
                    ans.append(str(left))
                if left < right:
                    ans.append(str(left) + '->' + str(right))
            left = val + 1
        return ans
