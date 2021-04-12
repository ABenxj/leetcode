#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/7 3:56 PM
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        创建一个新指针，依次比较大小
        :param l1:
        :param l2:
        :return:
        """
        ans = ListNode(0)
        ans_copy = ans
        while l1 and l2:
            if l1.val < l2.val:
                ans.next = l1
                l1 = l1.next
            else:
                ans.next = l2
                l2 = l2.next
            ans = ans.next
        if l1:
            ans.next = l1
        elif l2:
            ans.next = l2
        return ans_copy.next
