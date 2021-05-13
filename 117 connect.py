#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/13 8:45 上午
"""


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: Node) -> Node:
        """
        思路与116题类似；
        :param root:
        :return:
        """
        if not root:
            return root
        fathernode = root
        while fathernode:
            leftnode, curnode = None, None
            while fathernode:
                for node in [fathernode.left, fathernode.right]:
                    if node:
                        if not leftnode:
                            leftnode = node
                        if curnode:
                            curnode.next = node
                        curnode = node
                fathernode = fathernode.next
            fathernode = leftnode
        return root
