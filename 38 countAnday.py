#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/13 12:53 PM
"""


class Solution:

    def countAndSay(self, n: int) -> str:
        """
        依次遍历即可，注意临界条件
        :param n: 
        :return: 
        """
        s = '1'
        for _ in range(n-1):
            cur_char = s[0]
            count = 0
            s_next = ''
            for char in s:
                if cur_char == char:
                    count += 1
                else:
                    s_next += str(count)+cur_char
                    cur_char = char
                    count = 1
            s_next += str(count)+cur_char
            s = s_next
        return s
