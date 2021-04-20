#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/20 1:04 PM
"""


from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """

        :param intervals:
        :param newInterval:
        :return:
        """
        ans = []
        for i, pair in enumerate(intervals):
            if pair[0] > newInterval[1]:
                ans.append(newInterval)
                ans.extend(intervals[i:])
                break
            elif pair[1] < newInterval[0]:
                ans.append(pair)
            else:
                newInterval = [min(pair[0], newInterval[0]), max(pair[1], newInterval[1])]
        if not intervals or not ans or ans[-1][1] < newInterval[0]:
            ans.append(newInterval)
        return ans
