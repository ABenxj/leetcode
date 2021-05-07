#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/7 7:25 PM
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def inorderTraversal(self, root: TreeNode) -> List[int]:
        """
        递归解法
        :param root:
        :return:
        """
        ans = []

        def inorder(tree):
            """
            中序递归函数
            :param tree:
            :return:
            """
            if not tree:
                return None
            if tree.left:
                inorder(tree.left)
            ans.append(tree.val)
            if tree.right:
                inorder(tree.right)
        inorder(root)
        return ans

    def inorderTraversal_1(self, root: TreeNode) -> List[int]:
        """
        非递归解法，栈
        :param root:
        :return:
        """
        if not root:
            return []
        ans, stack, cur = [], [], root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            ans.append(cur.val)
            cur = cur.right
        return ans
