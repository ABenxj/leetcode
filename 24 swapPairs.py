#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 4:19 PM
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        """
        准备好三个指针，交换顺序，并依次向后遍历
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        ans = ListNode(0)
        ans.next = head
        pre, left, right = ans, head, head.next
        while True:
            left.next = right.next
            right.next = left
            pre.next = right
            if not left.next or not left.next.next:
                break
            pre, left, right = left, left.next, left.next.next
        return ans.next
