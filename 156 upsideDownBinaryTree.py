#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/27 10:11 上午
"""


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        """
        递归思想
        :param root:
        :return:
        """
        if not root or not root.left:
            return root
        left = self.upsideDownBinaryTree(root.left)
        root.left.left, root.left.right, root.left, root.right = self.upsideDownBinaryTree(root.right), root, None, None
        return left
