#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/17 1:12 PM
"""


class Solution:
    def decodeString(self, s: str) -> str:
        """
        递归思想，找出数字和对应括号内的字符串，并对字符串进行递归求解
        :param s:
        :return:
        """
        ret = ''
        i = 0
        while i < len(s):
            if s[i].isalpha():
                ret += s[i]
                i += 1
            elif s[i].isdigit():
                nums = 0
                while s[i].isdigit():
                    nums = nums*10 + int(s[i])
                    i += 1
            elif s[i] == '[':
                count = 1
                j = 1
                while count > 0:
                    if s[i+j] == '[':
                        count += 1
                    elif s[i+j] == ']':
                        count -= 1
                    j += 1
                ret += nums*self.decodeString(s[i+1:i+j-1])
                i += j
        return ret

    def decodeString_stack(self, s: str) -> str:
        """
        栈， 一共四类，字母、数字、[、]，注意每种情况的入栈、出栈和条件变更即可
        :param s:
        :return:
        """
        stack = []
        i, nums = 0, 0
        while i < len(s):
            if s[i].isalpha() or s[i] == '[':
                stack.append(s[i])
                i += 1
            elif s[i].isdigit():
                while s[i].isdigit():
                    nums = nums * 10 + int(s[i])
                    i += 1
                stack.append(nums)
                nums = 0
            elif s[i] == ']':
                cur_s = ''
                while True:
                    char = stack.pop()
                    if char == '[':
                        break
                    else:
                        cur_s = char + cur_s
                stack.append(stack.pop() * cur_s)
                i += 1
        return ''.join(stack)
