#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/5/28 11:14 上午
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        """

        :param headA:
        :param headB:
        :return:
        """
        if not headA or not headB: return None
        pa, pb = headA, headB
        while pa != pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa
