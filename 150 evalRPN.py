#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/26 7:34 上午
"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """

        :param tokens:
        :return:
        """
        ans = []
        while tokens:
            val = tokens.pop(0)
            if val.isdigit() or val[1:].isdigit():
                ans.append(int(val))
            else:
                val1 = ans.pop()
                val2 = ans.pop()
                cur = 0
                if val == '+':
                    cur = val1 + val2
                elif val == '-':
                    cur = val2 - val1
                elif val == '*':
                    cur = val2 * val1
                else:
                    cur = int(val2/val1)
                ans.append(cur)
        return ans[0]
