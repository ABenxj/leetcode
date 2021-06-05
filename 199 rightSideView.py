#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/6/5 5:46 下午
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def rightSideView(self, root: TreeNode) -> List[int]:
        """

        :param root:
        :return:
        """
        if not root:
            return []
        stack = [root]
        ans = []
        while stack:
            tree = stack[-1]
            ans.append(tree.val)
            index, len_s = 0, len(stack)
            while index < len_s:
                tree = stack.pop(0)
                if tree.left:
                    stack.append(tree.left)
                if tree.right:
                    stack.append(tree.right)
                index += 1
        return ans
