#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/30 9:46 下午
"""


class Solution:

    def compareVersion(self, version1: str, version2: str) -> int:
        """

        :param version1:
        :param version2:
        :return:
        """
        v1 = version1.split('.')
        v2 = version2.split('.')
        i, j = 0, 0
        while i < len(v1) or j < len(v2):
            v1_num = int(v1[i]) if i < len(v1) else 0
            v2_num = int(v2[j]) if j < len(v2) else 0
            if v1_num < v2_num:
                return -1
            elif v1_num > v2_num:
                return 1
            i += 1
            j += 1
        return 0
