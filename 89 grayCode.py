#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/7 9:07 AM
"""


from typing import List


class Solution:

    def grayCode(self, n: int) -> List[int]:
        """
        考虑n和n+1间的关系，类似于动态规划；
        :param n:
        :return:
        """
        ans, cur_head = [0], 1
        for _ in range(n):
            for i in range(len(ans)-1, -1, -1):
                ans.append(ans[i]+cur_head)
            cur_head *= 2
        return ans
