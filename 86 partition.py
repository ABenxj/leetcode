#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/30 5:41 PM
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        """
        双指针
        :param head:
        :param x:
        :return:
        """
        pre = ListNode(0, head)
        left, right = pre, pre
        while right.next:
            if right.next.val < x:
                if left == right:
                    left = left.next
                    right = right.next
                else:
                    left_next = left.next
                    left.next, right.next = right.next, right.next.next
                    left.next.next, left = left_next, left.next
            else:
                right = right.next
        return pre.next
