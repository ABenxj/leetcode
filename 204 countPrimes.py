#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/7 10:51 上午
"""


class Solution:
    def countPrimes(self, n: int) -> int:
        """
        构建1~n的数组，依次找出当前数的倍数，得到最后的的结果；
        :param n:
        :return:
        """
        if n < 3:
            return 0
        prime = [1]*n
        prime[:2] = [0, 0]
        prime[::2] = [0]*((n-1)//2+1)
        prime[2] = 1
        cur = 3
        while cur*cur < n:
            prime[cur*2::cur] = [0]*((n-1-cur*2)//cur+1)
            cur += 2
        return sum(prime)
