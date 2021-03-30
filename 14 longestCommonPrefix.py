#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/30
"""


from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        匹配各个字符串对应位置的字符是否相同，如果不同，则停止，注意字符串长度
        :param strs:
        :return:
        """
        if not strs:
            return ''
        prefix = ''
        cur_status = True
        cur_index = 0
        while cur_status:
            cur_char = None
            for s in strs:
                if cur_index >= len(s):
                    cur_status = False
                    break
                if cur_char is None:
                    cur_char = s[cur_index]
                elif cur_char != s[cur_index]:
                    cur_status = False
                    break
            if cur_status:
                prefix += cur_char
                cur_index += 1
        return prefix
