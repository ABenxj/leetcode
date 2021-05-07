#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/6 10:28 PM
"""


from typing import List


class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        回溯法
        :param nums:
        :return:
        """
        nums.sort()
        ans = []

        def back_trace(i, tmp):
            ans.append(tmp)
            for j in range(i, len(nums)):
                if j == i or nums[j] != nums[j-1]:
                    back_trace(j+1, tmp+nums[j:j+1])
        back_trace(0, [])
        return ans
