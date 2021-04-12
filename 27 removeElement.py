#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 4:37 PM
"""


from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """

        :param nums:
        :param val:
        :return:
        """
        index = 0
        for item in nums:
            if item != val:
                nums[index] = item
                index += 1
        return index
