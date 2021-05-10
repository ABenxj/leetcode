#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/10 10:21 上午
"""


import functools


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isBalanced(self, root: TreeNode) -> bool:
        """
        判断根节点左右节点的高度差，依次递归，记得采用functools；
        也可以直接在计算高度时进行判断，返回高度差，采用全局变量获取是否平衡的结果；
        :param root:
        :return:
        """
        if not root or (not root.left and not root.right):
            return True
        left_depth = self.get_depth(root.left)
        right_depth = self.get_depth(root.right)
        return abs(left_depth - right_depth) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    @functools.lru_cache()
    def get_depth(self, tree):
        """

        :param tree:
        :return:
        """
        if not tree:
            return 0
        return 1 + max(self.get_depth(tree.left), self.get_depth(tree.right))
