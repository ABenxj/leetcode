#!/usr/bin/env pyhton
# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 , Inc. All Rights Reserved
#

"""

Authors: jufei
Date:  
"""


# Definition for singly-linked list.
class ListNode:
    """
    链条节点
    """
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        """
        双指针，间隔n遍历
        :param head:
        :param n:
        :return:
        """
        ans = ListNode(0)
        ans.next = head
        left, right = ans, ans
        while right.next:
            if n == 0:
                left = left.next
            else:
                n -= 1
            right = right.next
        left.next = left.next.next
        return ans.next
