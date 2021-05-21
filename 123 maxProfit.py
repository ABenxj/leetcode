#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 5:03 下午
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """

        :param prices:
        :return:
        """
        dp = [[-prices[0], 0], [-prices[0], 0]]
        for price in prices:
            dp[0][0], dp[0][1] = max(dp[0][0], -price), max(dp[0][1], dp[0][0]+price)
            dp[1][0], dp[1][1] = max(dp[1][0], dp[0][1]-price), max(dp[1][1], dp[1][0]+price)
        return dp[1][1]
