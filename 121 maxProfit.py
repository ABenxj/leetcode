#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 12:57 下午
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        两个状态，一个买入，一个卖出
        :param prices:
        :return:
        """
        dp = [-prices[0], 0]
        for price in prices[1:]:
            dp[1] = max(dp[1], price + dp[0])
            dp[0] = max(dp[0], -price)
        return dp[1]
