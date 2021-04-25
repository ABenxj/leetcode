#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/25 2:31 PM
"""


from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        递归法
        :param nums:
        :return:
        """
        ans = []
        for i, val in enumerate(nums):
            ans.append([val])
            ans.extend([[val] + x for x in self.subsets(nums[i+1:]) if x])
        return [[]]+ans

    def subsets_2(self, nums: List[int]) -> List[List[int]]:
        """

        :param nums:
        :return:
        """
        ans = [[]]
        for val in nums:
            for j in range(len(ans)):
                ans.append(ans[j] + [val])
        return ans
