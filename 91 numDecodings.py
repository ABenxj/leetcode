#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/7 9:33 AM
"""


class Solution:

    def numDecodings(self, s: str) -> int:
        """
        动态规划，注意更新时，各种情况的判断
        :param s:
        :return:
        """
        if not s or s[0] == '0':
            return 0
        dp_pre, dp_ans = 1, 1
        for i in range(1, len(s)):
            cur_val = int(s[i-1:i+1])
            if cur_val % 10 == 0 and cur_val not in [10, 20]:
                return 0
            if 0 < cur_val < 10 or cur_val >= 27:
                dp_pre, dp_ans = dp_ans, dp_ans
            elif cur_val in [10, 20]:
                dp_pre, dp_ans = dp_ans, dp_pre
            elif 10 < cur_val < 27:
                dp_pre, dp_ans = dp_ans, dp_pre+dp_ans
        return dp_ans
