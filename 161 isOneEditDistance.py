#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/29 6:56 上午
"""


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        """
        依次比较对应位置，根据s和t字符的长短，选择不同的策略；
        :param s:
        :param t:
        :return:
        """
        s_l, t_l = len(s), len(t)
        if abs(s_l - t_l) > 1:
            return False

        i, j, ans = 0, 0, 0
        while i < s_l and j < t_l:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                ans += 1
                if s_l > t_l:
                    i += 1
                elif s_l < t_l:
                    j += 1
                else:
                    i += 1
                    j += 1
        return (ans == 1 and i == s_l and j == t_l) or (ans == 0 and (s_l - i) + (t_l - j) == 1)
