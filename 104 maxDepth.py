#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/9 10:07 上午
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def maxDepth(self, root: TreeNode) -> int:
        """
        递归求解
        :param root:
        :return:
        """
        if not root:
            return 0
        return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
