#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date: 2021/4/21 1:57 PM
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """
        双指针，间隔k， 如果k大于链表长度，需要遍历第二遍
        :param head:
        :param k:
        :return:
        """
        if not head:
            return head
        first_point = head
        second_point = head
        n = 0
        while first_point.next:
            first_point = first_point.next
            n += 1
            if k < n:
                second_point = second_point.next
        if k > n:
            k = k % (n+1)
            first_point = head
            second_point = head
            n = 0
            while first_point.next:
                first_point = first_point.next
                n += 1
                if k < n:
                    second_point = second_point.next
        first_point.next = head
        ans = second_point.next
        second_point.next = None
        return ans
