#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/25 2:05 PM
"""


from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """回溯法"""
        def backtrace(n, k, order):
            if k == 0:
                ans.append(order)
                return None
            if order and k + order[-1] > n:
                return None
            s_index = 0 if not order else order[-1]
            for i in range(s_index+1, n+1):
                backtrace(n, k-1, order+[i])
        ans = []
        backtrace(n, k, [])
        return ans

    def combine_2(self, n: int, k: int) -> List[List[int]]:
        """广度搜索"""
        ans = [[val] for val in range(1, n+1)]
        while k > 1:
            cur_len = len(ans)
            while cur_len > 0:
                cur_len -= 1
                tmp = ans.pop(0)
                if tmp[-1]+k-1 > n:
                    continue
                for val in range(tmp[-1]+1, n+1):
                    ans.append(tmp+[val])
            k -= 1
        return ans
