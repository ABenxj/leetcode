#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/30 4:18 PM
"""


# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        双指针，注意临界条件：空和最后一次更新；
        :param head:
        :return:
        """
        pre = ListNode(0, head)
        left, right, dup = pre, head, False
        while right and right.next:
            if left.next.val == right.next.val:
                dup = True
                right = right.next
            elif left.next.val != right.next.val:
                if dup:
                    left.next = right.next
                    right = right.next
                    dup = False
                else:
                    left = left.next
                    right = right.next
        if dup:
            left.next = None
        return pre.next
