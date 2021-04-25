#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/25 3:07 PM
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        双指针
        :param nums:
        :return:
        """
        slow = 1
        for fast in range(2, len(nums)):
            if nums[fast] > nums[slow] or nums[slow] != nums[slow-1]:
                slow += 1
                nums[slow] = nums[fast]
        return slow+1
