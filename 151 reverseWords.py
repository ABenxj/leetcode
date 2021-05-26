#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/26 7:53 上午
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        """

        :param s:
        :return:
        """
        s = [x for x in s.split(' ') if x]
        return ' '.join(s[::-1])
