#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/4/3
"""

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """

        :param nums:
        :param target:
        :return:
        """
        nums.sort()
        closest_sum = float('inf')
        for index, val in enumerate(nums[:-1]):
            if index > 0 and nums[index - 1] == val:
                continue
            left, right = index + 1, len(nums) - 1
            while left < right:
                nums_sum = val + nums[left] + nums[right]
                if nums_sum == target:
                    return target
                elif nums_sum > target:
                    right -= 1
                else:
                    left += 1
                if abs(closest_sum - target) > abs(nums_sum - target):
                    closest_sum = nums_sum
        return closest_sum

