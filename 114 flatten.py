#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/12 4:47 下午
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        递归算法，注意要把右节点关联；
        :param root:
        :return:
        """
        if not root:
            return None
        left = root.left
        right = root.right
        root.left = None
        root.right = left
        self.flatten(left)
        while root.right:
            root = root.right
        root.right = right
        self.flatten(right)

    def flatten_stack(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        栈，依次压缩，先进后出，也可以用队列，一样的。
        :param root:
        :return:
        """
        stack = [root] if root else []
        while stack:
            tree = stack.pop()
            if tree.right:
                stack.append(tree.right)
            if tree.left:
                stack.append(tree.left)
            if tree == root:
                pre = root
            else:
                pre.left = None
                pre.right = tree
                pre = pre.right
