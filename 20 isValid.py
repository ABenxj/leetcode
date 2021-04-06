#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date:
"""


class Solution:
    def isValid(self, s: str) -> bool:
        """
        使用栈
        :param s:
        :return:
        """
        brackets = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        stack = []
        for bracket in s:
            if bracket in brackets:
                stack.append(bracket)
            elif not stack or brackets[stack.pop()] != bracket:
                return False
        return stack == []
