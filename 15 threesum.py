#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/30
"""


from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        for循环+双指针，注意优化，可以减少重复计算
        :param nums:
        :return:
        """
        nums.sort()
        ret = []
        cur_i = 0
        for cur_i in range(len(nums)-2):
            if nums[cur_i] > 0:
                break
            if cur_i > 0 and nums[cur_i] == nums[cur_i-1]:
                continue
            l, r = cur_i+1, len(nums)-1
            while l < r:
                s = nums[cur_i]+nums[l]+nums[r]
                if s == 0:
                    ret.append([nums[cur_i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    r -= 1
            cur_i = cur_i+1
        return ret