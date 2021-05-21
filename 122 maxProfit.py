#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 4:37 下午
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        :param prices:
        :return:
        """
        dp = [-prices[0], 0]
        for price in prices:
            tmp = dp[1]
            dp[1] = max(dp[1], price+dp[0])
            dp[0] = max(dp[0], tmp-price)
        return dp[1]
