#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/26 5:36 下午
"""


from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curmin, curmax, ans = 1, 1, -float('inf')
        for val in nums:
            curmin, curmax = min(curmax*val, val, curmin*val), max(curmax*val, val, curmin*val)
            ans = max(ans, curmax)
        return ans
