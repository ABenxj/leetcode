#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/7 5:37 下午
"""


import collections
from typing import List


class Solution:

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        有向图，dfs，visited需要三种状态， bfs: 看节点的度即可，
        :param numCourses:
        :param prerequisites:
        :return:
        """
        edge = collections.defaultdict(list)
        visited = collections.defaultdict(int)
        for i, j in prerequisites:
            edge[j].append(i)
            visited[i] += 1
        queue = [i for i in range(numCourses) if i not in visited]
        valid_course = 0
        while queue:
            cur_course = queue.pop(0)
            valid_course += 1
            for i in edge[cur_course]:
                visited[i] -= 1
                if visited[i] == 0:
                    queue.append(i)
        return valid_course == numCourses
