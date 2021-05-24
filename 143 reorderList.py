#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/24 10:20 上午
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        分三步，第一步：找出中间点（注意临界条件）， 第二步：后半部分链表反转， 第三步：合并
        :param head:
        :return:
        """
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        if not slow or not slow.next:
            return None
        post, slow.next = slow.next, None
        pre = None
        while post:
            post.next, post, pre = pre, post.next, post
        post = pre
        while post:
            head.next, post.next, head, post = post, head.next, head.next, post.next
        return None
