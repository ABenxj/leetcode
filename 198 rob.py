#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/5 5:17 下午
"""


from typing import  List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """

        :param nums:
        :return:
        """
        ans, pre_df = 0, 0
        for val in nums:
            ans, pre_df = max(ans, pre_df+val), ans
        return ans
