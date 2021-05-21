#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 5:13 下午
"""


from typing import List


class Solution:

    def maxProfit(self, k: int, prices: List[int]) -> int:
        """

        :param k:
        :param prices:
        :return:
        """
        if not prices or k == 0:
            return 0
        dp_buy = [-prices[0] for _ in range(k)]
        dp_sell = [0 for _ in range(k)]
        for price in prices:
            for i in range(k):
                dp_buy[i], dp_sell[i] = max(
                    dp_buy[i],
                    dp_sell[i-1]-price if i > 0 else -price
                ), max(
                    dp_sell[i],
                    dp_buy[i] + price
                )
        return max(dp_sell)
