#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 5:39 下午
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """

        :param prices:
        :param fee:
        :return:
        """
        dp = [-prices[0], 0]
        for price in prices:
            dp = [
                max(dp[0], dp[1]-price),
                max(dp[1], dp[0]+price-fee)
            ]
        return dp[1]
