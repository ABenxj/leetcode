#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 9:27 下午
"""


from typing import List


class Solution:

    def singleNumber(self, nums: List[int]) -> int:
        """
        异或运算的运用；
        :param nums:
        :return:
        """
        cur = 0
        for num in nums:
            cur ^= num
        return cur