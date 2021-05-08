#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/8 10:09 PM
"""


from typing import List


class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        回溯法
        :param s:
        :return:
        """
        ans = []

        def back_trace(order, s):
            """
            递归函数
            :param order:
            :param s:
            :return:
            """
            if len(order) == 4 and not s:
                ans.append('.'.join(order))
            if len(order) > 4 or not s:
                return None
            if len(s) >= 1:
                back_trace(order+[s[:1]], s[1:])
            if len(s) >= 2:
                if int(s[:2]) >= 10:
                    back_trace(order+[s[:2]], s[2:])
            if len(s) >= 3:
                if 100 <= int(s[:3]) <= 255:
                    back_trace(order+[s[:3]], s[3:])
        back_trace([], s)

        return ans
