#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/23
"""
"""
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。

回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。例如，121 是回文，而 123 不是。

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        """
        双指针，从两边往中间遍历
        :param x:
        :return:
        """
        s = str(x)
        left, right = 0, len(s)-1
        while left <= right and s[left] == s[right]:
            left += 1
            right -= 1
        return left > right
