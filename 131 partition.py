#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 7:32 下午
"""


import functools
from typing import List


class Solution:
    @functools.lru_cache()
    def partition(self, s: str) -> List[List[str]]:
        """

        :param s:
        :return:
        """
        ans = []
        if not s:
            return [[]]
        for i in range(len(s)):
            if s[:i+1] == s[:i+1][::-1]:
                ans.extend([[s[:i+1]] + x for x in self.partition(s[i+1:])])
        return ans
