#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/31 8:15 上午
"""


class Solution:

    def titleToNumber(self, columnTitle: str) -> int:
        """

        :param columnTitle:
        :return:
        """
        ans = 0
        for alpha in columnTitle:
            ans = ans*26 + ord(alpha)-64
        return ans

