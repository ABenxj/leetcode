#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/8 8:13 上午
"""


from typing import List


class Solution:

    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        """
        双指针
        :param s:
        :param nums:
        :return:
        """
        l, r, ans = 0, 0, float('inf')
        n_sum = 0
        while r < len(nums):
            n_sum += nums[r]
            while n_sum-nums[l] >= s and l<r:
                n_sum -= nums[l]
                l += 1
            if n_sum >= s:
                ans = min(ans, r-l+1)
            r += 1
        return ans if ans < float('inf') else 0
