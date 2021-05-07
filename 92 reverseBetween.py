#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/7 10:19 AM
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        """
        双指针
        :param head:
        :param left:
        :param right:
        :return:
        """
        if left == right:
            return head
        ans = ListNode(0, head)
        p_a, p_b = ans, head
        cur_num = 0
        while cur_num <= right:
            if cur_num == left-1:
                p_left = p_a
                p_a, p_b = p_b, p_b.next
                p_a.next = None
            elif cur_num < left-1:
                p_a, p_b = p_b, p_b.next
            elif cur_num == right:
                p_left.next.next, p_left.next = p_b, p_a
            elif cur_num >= left:
                p_b_tmp = p_b.next
                p_b.next = p_a
                p_a, p_b = p_b, p_b_tmp
            cur_num += 1
        return ans.next
