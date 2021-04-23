#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/23 4:07 PM
"""


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        双指针做法；思路比较简单，但是临界值可能比较麻烦；
        :param nums:
        :return:
        """
        """
        Do not return anything, modify nums in-place instead.
        """
        left, right, cur = 0, len(nums) - 1, 0
        while cur <= right:
            if nums[cur] == 0:
                nums[cur], nums[left] = nums[left], nums[cur]
                while left <= right and nums[left] == 0:
                    left += 1
                cur = max(left, cur + 1)
            elif nums[cur] == 2:
                nums[cur], nums[right] = nums[right], nums[cur]
                while left <= right and nums[right] == 2:
                    right -= 1
            else:
                cur += 1
