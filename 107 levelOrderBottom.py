#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/10 9:11 上午
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        """
        与102题几乎完全相同
        :param root:
        :return:
        """
        ans = []
        stack = [root]
        while stack:
            cur_level = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node:
                    cur_level.append(node.val)
                    stack.extend([node.left, node.right])
            if cur_level:
                ans.append(cur_level)
        return ans[::-1]
