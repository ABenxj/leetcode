#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/29 6:57 上午
"""


from typing import List


class Solution:

    def findPeakElement(self, nums: List[int]) -> int:
        """
        二分法， 注意临界条件， nums[-1], nums[n]均为负无穷；
        :param nums:
        :return:
        """
        l, r = 0, len(nums)-1
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1
        return r
