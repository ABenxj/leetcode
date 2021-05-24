#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/24 9:52 上午
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        """
        与前序遍历类似，可以使用递归或者栈，用栈时，注意pop和push的顺序；
        :param root:
        :return:
        """
        stack, ans = [root], []
        while stack:
            tree = stack.pop()
            if tree:
                ans.append(tree.val)
                stack.append(tree.left)
                stack.append(tree.right)
        return ans[::-1]