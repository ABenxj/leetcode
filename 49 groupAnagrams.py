#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/17 3:46 PM
"""


from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        直接排序，作为hash的key； 另一种方法：考虑26个字母计数作为key
        :param strs:
        :return:
        """
        ans = {}
        for s in strs:
            s_key = ''.join(sorted(s))
            if s_key in ans:
                ans[s_key].append(s)
            else:
                ans[s_key] = [s]
        return list(ans.values())
