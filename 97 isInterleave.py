#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/8 8:37 PM
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        思路1： 深度搜索，如果匹配上，返回True
        思路2： 动态规划，二维数组，每个值代表对应的位置是否可行；
        思路3： 动态规划，记录下S3每一步可以匹配的位置，依次更新；
        :param s1:
        :param s2:
        :param s3:
        :return:
        """
        ans = [(-1, -1)]
        index = 0
        while index < len(s3):
            tmp = set()
            for i, j in ans:
                if i+1 < len(s1) and s1[i+1] == s3[index]:
                    tmp.add((i+1, j))
                if j+1 < len(s2) and s2[j+1] == s3[index]:
                    tmp.add((i, j+1))
            index += 1
            ans = list(tmp)
            print(ans)
        return bool(ans) and ans[0][0]+ans[0][1] == len(s1)+len(s2)-2
