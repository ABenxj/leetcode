#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/9 9:48 上午
"""


from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        trees = [root]
        while trees:
            cur_level = []
            new_trees = []
            for tree in trees:
                if tree:
                    cur_level.append(tree.val)
                    new_trees.extend([tree.left, tree.right])
            trees = new_trees
            if cur_level:
                ans.append(cur_level)
        return ans
