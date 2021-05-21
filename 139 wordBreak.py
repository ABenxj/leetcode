#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/21 10:14 下午
"""


from typing import List


class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        dp思想
        :param s:
        :param wordDict:
        :return:
        """
        dp = [True]+[False]*len(s)
        for i, _ in enumerate(dp):
            for word in wordDict:
                dp[i] = dp[i] or (dp[i-len(word)] and s[i-len(word):i]==word)
        return dp[-1]
