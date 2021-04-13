#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/13 12:10 PM
"""


from typing import List


class Solution:

    def searchInsert(self, nums: List[int], target: int) -> int:
        """
        二分查找
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        return left
