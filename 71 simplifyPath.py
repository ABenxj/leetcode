#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/22 2:13 PM
"""


class Solution:
    def simplifyPath(self, path: str) -> str:
        """

        :param path:
        :return:
        """
        ans = []
        for val in path.split('/'):
            if val == '.' or not val:
                continue
            elif val == '..':
                if ans:
                    ans.pop()
            else:
                ans.append(val)
        return '/'+'/'.join(ans)
