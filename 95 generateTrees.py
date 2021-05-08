#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/8 9:07 PM
"""


import functools
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        """
        分为左右两侧，分别递归；
        :param n:
        :return:
        """
        @functools.lru_cache()
        def preorder(i, j):
            """
            递归函数
            :param i:
            :param j:
            :return:
            """
            if i > j:
                return [None]
            if i == j:
                return [TreeNode(i, None, None)]
            subtrees = []
            for val in range(i, j+1):
                for left in preorder(i, val-1):
                    for right in preorder(val+1, j):
                        subtrees.append(TreeNode(val, left, right))
            return subtrees

        return preorder(1, n)
