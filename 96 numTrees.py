#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/8 8:46 PM
"""


class Solution:
    def numTrees(self, n: int) -> int:
        """
        动态规划，把树按照根节点分成左右两个部分；
        :param n:
        :return:
        """
        dp = [1] + [0]*n
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1]*dp[i-j]
        return dp[-1]
