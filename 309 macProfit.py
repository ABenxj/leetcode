#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 5:34 下午
"""


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        如果冷冻期为多天，可以考虑扩大dp数组；
        :param prices:
        :return:
        """
        dp_buy = [-prices[0], -prices[0]]
        dp_sell = [0, 0]
        for price in prices:
            dp_buy[0], dp_buy[1] = dp_buy[1], max(dp_buy[1], dp_sell[0]-price)
            dp_sell[0], dp_sell[1] = dp_sell[1], max(dp_sell[1], dp_buy[0]+price)
        return dp_sell[1]
