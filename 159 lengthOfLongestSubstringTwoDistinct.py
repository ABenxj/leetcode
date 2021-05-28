#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/28 11:15 上午
"""


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        """
        dp思想，f(n) = max(f(n-1), g(s[n])), f表示前n个字符串的结果， g表示前n个字符串中，包含最后一个字符的结果；
        :param s:
        :return:
        """
        ans, cur_s, cur_num = 0, {}, 0
        cur_ans = 0
        for i, val in enumerate(s):
            if val in cur_s:
                cur_s[val] = i
                cur_ans += 1
            elif cur_num < 2:
                cur_s[val] = i
                cur_num += 1
                cur_ans += 1
            else:
                index = min(cur_s.values())
                cur_s.pop(s[index])
                cur_s[val] = i
                cur_num = 2
                cur_ans = i - index
            ans = max(ans, cur_ans)
        return ans
