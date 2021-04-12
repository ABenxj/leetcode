#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 5:34 PM
"""


from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        第一步，依次从后向前，找出第一个变小的数的位置和值； 第二步，找出比该值大的最后一个数，对换位置，排序
        :param nums:
        :return:
        """
        index = len(nums) - 2
        while index >= 0 and nums[index] >= nums[index+1]:
            index -= 1
        if index < 0:
            nums[:] = nums[::-1]
            return None
        interval = 1
        while index+interval < len(nums) and nums[index] < nums[index+interval]:
            interval += 1
        nums[index], nums[index+interval-1] = nums[index+interval-1], nums[index]
        nums[index+1:] = nums[index+1:][::-1]
        return None

