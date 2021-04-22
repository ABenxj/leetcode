#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/22 1:17 PM
"""


from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        add
        :param digits:
        :return:
        """
        num = 1
        for i in range(len(digits)-1, -1, -1):
            num, digits[i] = divmod(digits[i]+num, 10)
            if num == 0:
                break
        if num > 0:
            digits.insert(0, num)
        return digits
