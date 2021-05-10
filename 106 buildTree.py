#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/10 8:57 上午
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        """
        递归，与上一题基本完全相似
        :param inorder:
        :param postorder:
        :return:
        """
        if not inorder:
            return None
        index = inorder.index(postorder[-1])
        return TreeNode(
            postorder[-1],
            self.buildTree(inorder[:index], postorder[:index]),
            self.buildTree(inorder[index+1:], postorder[index:-1])
        )
