#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/9 10:17 上午
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        找出根节点，左右两部分，递归；
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder:
            return None
        i = inorder.index(preorder[0])
        return TreeNode(
            preorder[0],
            self.buildTree(preorder[1:i+1], inorder[:i]),
            self.buildTree(preorder[i+1:], inorder[i+1:])
        )
