#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/10 9:45 上午
"""

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        """
        找到根节点和左右部分，直接递归；
        :param nums:
        :return:
        """
        if not nums:
            return None
        half = (len(nums)-1)//2
        return TreeNode(
            nums[half],
            self.sortedArrayToBST(nums[:half]),
            self.sortedArrayToBST(nums[half+1:])
        )
