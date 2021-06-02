#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/3 5:41 上午
"""


from typing import List


class Solution:

    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        翻转两次，先全体翻转，再词内翻转；
        :param s:
        :return:
        """
        s[:] = s[::-1]
        left, right = 0, 0
        while right < len(s):
            if s[right] == " ":
                s[left:right] = s[left:right][::-1]
                left, right = right+1, right+1
            else:
                right += 1
        s[left:] = s[left:][::-1]
