#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/30 12:27 下午
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        """
        ascii码的装换，ord和chr函数；
        :param columnNumber:
        :return:
        """
        ans = []
        while columnNumber > 0:
            columnNumber, mod = divmod(columnNumber-1, 26)
            ans.append(chr(65+mod))
        return ''.join(ans[::-1])
