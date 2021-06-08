#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/7 9:51 上午
"""


class Solution:

    def isHappy(self, n: int) -> bool:
        """
        按公式计算即可
        :param n:
        :return:
        """
        visited = set()
        visited.add(1)
        while n not in visited:
            visited.add(n)
            new_n = 0
            while n > 0:
                n, mod = divmod(n, 10)
                new_n += mod*mod
            n = new_n
        return n == 1
