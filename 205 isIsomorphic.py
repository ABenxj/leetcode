#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/7 11:12 上午
"""


class Solution:

    def isIsomorphic(self, s: str, t: str) -> bool:
        """
        注意是同构关系，一一映射
        :param s:
        :param t:
        :return:
        """
        charmap = dict()
        charmap_1 = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] not in charmap:
                charmap[s[i]] = t[i]
            elif charmap[s[i]] != t[i]:
                return False
            if t[i] not in charmap_1:
                charmap_1[t[i]] = s[i]
            elif charmap_1[t[i]] != s[i]:
                return False
        return True
