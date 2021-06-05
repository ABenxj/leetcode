#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/5 6:02 下午
"""


from typing import List


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        """
        新建了一个visited矩阵，来记录访问状态，也可以考虑直接改为'0'，节约空间；
        :param grid:
        :return:
        """
        if not grid or not grid[0]:
            return 0
        row, col = len(grid), len(grid[0])
        visited = [[0 for _ in range(col)] for _ in range(row)]
        ans = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1' and visited[i][j] == 0:
                    ans += 1
                    stack = [(i, j)]
                    while stack:
                        cur_i, cur_j = stack.pop()
                        if visited[cur_i][cur_j] == 1:
                            continue
                        visited[cur_i][cur_j] = 1
                        for diff_i, diff_j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                            next_i, next_j = cur_i+diff_i, cur_j+diff_j
                            if 0 <= next_i < row and 0 <= next_j < col and \
                                    visited[next_i][next_j] == 0 and grid[next_i][next_j] == '1':
                                stack.append((next_i, next_j))
                else:
                    visited[i][j] = 1
        return ans
