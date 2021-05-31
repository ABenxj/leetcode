#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/30 10:12 下午
"""


class Solution:

    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        """
        注意考虑各种边界情况；
        :param numerator:
        :param denominator:
        :return:
        """
        sign = '-' if numerator*denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        div, mod = divmod(numerator, denominator)
        if mod == 0:
            return sign + str(div)
        mods = {}
        ans, index = [], 0
        while mod not in mods:
            mods[mod] = index
            index += 1
            mod = 10*mod
            new_div, mod = divmod(mod, denominator)
            ans.append(str(new_div))
            if mod == 0:
                return sign + str(div)+'.'+''.join(ans)
        return sign + str(div)+'.' + ''.join(ans[:mods[mod]]) + '('+''.join(ans[mods[mod]:])+')'
