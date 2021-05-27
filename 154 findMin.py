#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/27 9:37 上午
"""


from typing import List


class Solution:

    def findMin(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        low = 0
        high = len(nums)-1
        while high > low:
            pivot = low + (high - low) // 2
            # Case 1):
            if nums[pivot] < nums[high]:
                high = pivot
            # Case 2):
            elif nums[pivot] > nums[high]:
                low = pivot + 1
            # Case 3):
            else:
                high -= 1
        # the 'low' and 'high' index converge to the inflection point.
        return nums[low]
