#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/1 9:58 上午
"""


from typing import List


class Solution:

    def largestNumber(self, nums: List[int]) -> str:
        """
        结合快排
        :param nums:
        :return:
        """
        self.quick_sort(nums, 0, len(nums) - 1)
        return ''.join([str(x) for x in nums]) if nums[0] > 0 else '0'

    def quick_sort(self, nums, start, end):
        """

        :param nums:
        :param start:
        :param end:
        :return:
        """
        if start >= end:
            return None
        cur, val, = start, nums[start]
        n_c = 10
        while n_c <= val:
            n_c *= 10
        for i in range(start + 1, end + 1):
            n = 10
            while n <= nums[i]:
                n *= 10
            if n * val + nums[i] < n_c * nums[i] + val:
                cur += 1
                nums[cur], nums[i] = nums[i], nums[cur]
        nums[start], nums[cur] = nums[cur], nums[start]
        self.quick_sort(nums, start, cur - 1)
        self.quick_sort(nums, cur + 1, end)
