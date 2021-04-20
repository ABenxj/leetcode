#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/20 12:21 PM
"""


from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        先排序，再依次比较前后两个数组是否相交
        :param intervals:
        :return:
        """
        intervals.sort(key=lambda x: x[0])
        ans = [intervals[0]]
        for interval_item in intervals[1:]:
            if ans[-1][1] < interval_item[0]:
                ans.append(interval_item)
            else:
                ans[-1][1] = max(ans[-1][1], interval_item[1])
        return ans
