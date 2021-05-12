#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/12 12:12 下午
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        """
        递归，sum为内建关键字，自己使用python编程时应注意
        :param root:
        :param sum:
        :return:
        """
        if not root:
            return False
        if not root.left and not root.right:
            return sum == root.val
        ans = False
        if root.left:
            ans = ans or self.hasPathSum(root.left, sum - root.val)
        if root.right:
            ans = ans or self.hasPathSum(root.right, sum - root.val)
        return ans
