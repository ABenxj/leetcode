#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/22 1:54 PM
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        """
        二分查找
        :param x:
        :return:
        """
        left, right = 1, x
        while left <= right:
            mid = (left + right) // 2
            val = x // mid
            if val == mid:
                return mid
            elif val > mid:
                left = mid + 1
            else:
                right = mid - 1
        return right
