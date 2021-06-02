#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/3 5:43 上午
"""


from collections import defaultdict
from typing import List


class Solution:

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        """
        hash存储，时间空间复杂度都为O(n*l)
        :param s:
        :return:
        """
        s_dict = defaultdict(int)
        ans = []
        for i in range(len(s)-9):
            s_dict[s[i:i+10]] += 1
        for key, val in s_dict.items():
            if val > 1:
                ans.append(key)
        return ans
