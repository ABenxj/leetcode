#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 4:32 PM
"""


from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        cur_val, i = float('inf'), 0
        for val in nums:
            if cur_val != val:
                nums[i] = val
                cur_val = val
                i += 1
        return i
