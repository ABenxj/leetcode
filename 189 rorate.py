#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/3 6:16 上午
"""


from typing import List


class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        方法有多种：
        1、利用python特性，直接翻转指定部分并拼接；
        2、额外申请空间，保存指定部分，在拼接（同一）
        3、环形替换，位置i放到i+k，依次替换，直到形成环停止；再继续遍历下一个环；
        4、多次翻转
        :param nums:
        :param k:
        :return:
        """
        # 方法1、2
        k = k % len(nums)
        nums[:] = nums[-k:]+nums[:-k]

        # 方法 4
        k = k % len(nums)
        nums[:] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
