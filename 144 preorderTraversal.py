#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/24 9:47 上午
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def preorderTraversal(self, root: TreeNode) -> List[int]:
        """
        两种思路，一种是递归（比较简单），另一种是迭代，
        :param root:
        :return:
        """
        stack, ans = [root], []
        while stack:
            tree = stack.pop()
            if tree:
                ans.append(tree.val)
                stack.append(tree.right)
                stack.append(tree.left)
        return ans
