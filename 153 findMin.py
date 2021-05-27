#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/27 8:04 上午
"""


from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        二分查找，注意临界条件
        :param nums:
        :return:
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[r] < nums[l] <= nums[mid]:
                l = mid + 1
            else:
                r = mid
        return nums[l]
