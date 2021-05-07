#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/30 4:15 PM
"""


from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        """
        二分查找，注意特殊情况；左、右、中间节点的值，都相等的情况
        :param nums:
        :param target:
        :return:
        """
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                return True
            if nums[left] == nums[mid] and nums[mid] == nums[right]:
                left = left + 1
                right = right - 1
                continue
            if nums[mid] >= nums[left]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
