#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/10 10:36 上午
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def sortedListToBST(self, head: ListNode) -> TreeNode:
        """

        :param head:
        :return:
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow,fast = head, head.next.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        cur, slow.next = slow.next, None
        return TreeNode(
            cur.val,
            self.sortedListToBST(head),
            self.sortedListToBST(cur.next)
        )
