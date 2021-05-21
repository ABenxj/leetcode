#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/17 5:40 下午
"""


from typing import List


class Solution:
    def backtrace(self, i, j, board, visited, ensure):
        """
        递归函数
        :param i:  当前横坐标；
        :param j:  当前纵坐标；
        :param board:  
        :param visited: 标记访问过的位置；
        :param ensure: 确定为'O'的位置点；
        :return:
        """
        visited[i][j] = 1
        if board[i][j] == 'O':
            ensure[i][j] = 1
        else:
            return None
        for m, n in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            next_i, next_j = i + m, j + n
            if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) and not visited[next_i][next_j]:
                self.backtrace(next_i, next_j, board, visited, ensure)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[0 for _ in board[0]] for _ in board]
        ensure = [[0 for _ in board[0]] for _ in board]
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O' and not \
                visited[i][j]:
                    self.backtrace(i, j, board, visited, ensure)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if ensure[i][j] == 0 and board[i][j] == 'O':
                    board[i][j] = 'X'
