#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/25 4:13 PM
"""


from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        深度优先搜索，注意已经访问过的节点
        :param board:
        :param word:
        :return:
        """
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(board, cur_i, cur_j, check_word, visited):
            if board[cur_i][cur_j] != check_word[0]:
                return False
            if len(check_word) == 1:
                return True
            visited.add((cur_i, cur_j))
            for x, y in directions:
                next_i, next_j = cur_i+x, cur_j+y
                if 0 <= next_i < len(board) and 0 <= next_j < len(board[0]) and (next_i, next_j) not in visited \
                        and dfs(board, next_i, next_j, check_word[1:], visited):
                    return True
            visited.remove((cur_i, cur_j))
            return False

        visited = set()
        for i, _ in enumerate(board):
            for j, _ in enumerate(board[0]):
                if dfs(board, i, j, word, visited):
                    return True
        return False
