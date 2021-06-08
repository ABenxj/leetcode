#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/8 8:16 上午
"""


from collections import defaultdict
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """

        :param numCourses:
        :param prerequisites:
        :return:
        """
        edge = defaultdict(list)
        degree = defaultdict(int)
        for crs_1, crs_2 in prerequisites:
            edge[crs_2].append(crs_1)
            degree[crs_1] += 1
        queue = [cr_id for cr_id in range(numCourses) if cr_id not in degree]
        ans = []
        while queue:
            cur_cr = queue.pop(0)
            ans.append(cur_cr)
            for next_cr in edge[cur_cr]:
                degree[next_cr] -= 1
                if degree[next_cr] == 0:
                    queue.append(next_cr)
        return ans if len(ans) == numCourses else []
