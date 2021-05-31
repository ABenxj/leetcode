#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/31 10:14 上午
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.ans = []
        self.index = 0
        self._init(root)

    def _init(self, root):
        if not root:
            return None
        self._init(root.left)
        self.ans.append(root.val)
        self._init(root.right)

    def next(self) -> int:
        self.index += 1
        return self.ans[self.index - 1]

    def hasNext(self) -> bool:
        if self.index < len(self.ans):
            return True
        return False

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
