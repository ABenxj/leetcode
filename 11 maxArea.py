#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/24
"""


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        双指针，注意更新条件即可；
        :param height:
        :return:
        """
        l, r = 0, len(height) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, (r - l) * min(height[l], height[r]))
            i, j = 0, 0
            if height[l] <= height[r]:
                while l+i < r and height[l+i] <= height[l]:
                    i += 1
            if height[l] >= height[r]:
                while l < r-j and height[r-j] <= height[r]:
                    j += 1
            l += i
            r -= j
        return max_area
