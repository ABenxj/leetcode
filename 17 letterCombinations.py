#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/4/3
"""


from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        广度搜索
        :param digits:
        :return:
        """
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        lc = ['']
        for s in digits:
            lc_len = len(lc)
            while lc_len>0:
                lc_len -= 1
                cur_lc = lc.pop(0)
                for char in phoneMap[s]:
                    lc.append(cur_lc+char)
        return lc

    def letterCombinations_backtrace(self, digits: str) -> List[str]:
        """
        回溯法（深度搜索）
        :param digits:
        :return:
        """
        if not digits:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
