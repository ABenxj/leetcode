#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/15 4:44 下午
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        """
        回溯法
        :param root:
        :return:
        """

        ans = []

        def backtrace(root, val):
            """
            递归函数
            :param root:
            :param val:
            :return:
            """
            if not root.left and not root.right:
                ans.append(val * 10 + root.val)
                return None
            if root.left:
                backtrace(root.left, val * 10 + root.val)
            if root.right:
                backtrace(root.right, val * 10 + root.val)

        backtrace(root, 0)
        return sum(ans)
