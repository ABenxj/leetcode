#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/8 7:49 PM
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        思路一：中序遍历， 看看结果是不是顺序的；
        思路二：判断每棵树是否满足最大最小值；
        :param root:
        :return:
        """

        def isValid(tree, min_val, max_val):
            """
            递归判断函数
            :param tree:
            :param min_val:
            :param max_val:
            :return:
            """
            if not tree:
                return True
            ans = min_val < tree.val < max_val
            if tree.left:
                ans = ans and isValid(tree.left, min_val, tree.val)
            if tree.right:
                ans = ans and isValid(tree.right, tree.val, max_val)
            return ans

        return isValid(root, -float('inf'), float('inf'))
