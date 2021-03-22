#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved
#

"""


Authors: jufei@baidu.com
Date:    2021/3/22
"""
"""
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。

如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1
        x = abs(x)
        ret = 0
        while x:
            x, mod = divmod(x, 10)
            ret = ret*10 + mod
        ret = ret*sign
        return ret if -2**31 <= ret <= 2**31 - 1 else 0
