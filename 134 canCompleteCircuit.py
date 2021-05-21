#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 8:43 下午
"""


from typing import List


class Solution:

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        """
        遍历一遍，依次求和，最低点的下一个位置，就是起始位置；
        :param gas:
        :param cost:
        :return:
        """
        all_sum, min_sum = 0, float('inf')
        for i in range(len(gas)):
            cur_diff = gas[i]-cost[i]
            all_sum += cur_diff
            if all_sum <= min_sum:
                min_sum = all_sum
                index = i
        return (index+1) % len(gas) if all_sum >= 0 else -1
