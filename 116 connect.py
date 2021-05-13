#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/13 8:25 上午
"""


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:

    def connect(self, root: Node) -> Node:
        """
        结合left、right和next之间的关系
        :param root:
        :return:
        """
        if not root:
            return root
        leftnode = root
        while leftnode.left:
            head = leftnode
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftnode = leftnode.left
        return root
