#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/9 9:36 上午
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def isSymmetric(self, root: TreeNode) -> bool:
        """
        递归思想，依次判断
        :param root:
        :return:
        """
        def issym(left, right):
            """
            递归判断函数
            :param left:
            :param right:
            :return:
            """
            if left and right and left.val == right.val:
                ans = True
                return issym(left.left, right.right) and issym(left.right, right.left)
            if not left and not right:
                return True
            return False
        return issym(root.left, root.right) if root else True
