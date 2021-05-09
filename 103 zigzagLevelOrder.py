#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/9 10:03 上午
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """
        与上一题方法类似，注意对应行倒序排列即可；
        :param root:
        :return:
        """
        ans = []
        trees = [root]
        level = 0
        while trees:
            cur_level = []
            for _ in range(len(trees)):
                tree = trees.pop(0)
                if tree:
                    if level%2 == 0:
                        cur_level.append(tree.val)
                    else:
                        cur_level.insert(0, tree.val)
                    trees.extend([tree.left, tree.right])
            if cur_level:
                ans.append(cur_level)
            level += 1
        return ans
