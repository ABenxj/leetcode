#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/13 11:55 AM
"""


from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        """
        二分查找，先查左边界，再查右边界
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left + right) // 2
            if target <= nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        index_min = left
        if not nums or index_min >= len(nums) or nums[index_min] != target:
            return [-1, -1]
        left, right = index_min, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if target >= nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return [index_min, right]
